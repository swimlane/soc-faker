import sys
import binascii, base64
from io import BytesIO

from .network import Network

#Custom Foo Protocol Packet
__MESSAGE__ =  ('01 01 00 08'   #Foo Base Header
                '01 02 00 00'   #Foo Message (31 Bytes)
                '00 00 12 30'   
                '00 00 12 31'
                '00 00 12 32' 
                '00 00 12 33' 
                '00 00 12 34' 
                'D7 CD EF'      #Foo flags
                '00 00 12 35')     


class PCAP(object):

    @property
    def __global_header(self):
        return ('D4 C3 B2 A1'   
                '02 00'         #File format major revision (i.e. pcap <2>.4)  
                '04 00'         #File format minor revision (i.e. pcap 2.<4>)   
                '00 00 00 00'     
                '00 00 00 00'     
                'FF FF 00 00'     
                '01 00 00 00')

    @property
    def __packet_header(self):
        #pcap packet header that must preface every packet
        return ('AA 77 9F 47'     
                '90 A2 04 00'     
                'XX XX XX XX'   #Frame Size (little endian) 
                'YY YY YY YY')  #Frame Size (little endian)

    @property
    def __ethernet_header(self):
        return ('00 00 00 00 00 00'     #Source Mac    
                '00 00 00 00 00 00'     #Dest Mac  
                '08 00')                #Protocol (0x0800 = IP)

    @property
    def __ip_header(self):
        source_ip = Network(private=True).ipv4.split('.')
        source_ip_hex = '{:02X} {:02X} {:02X} {:02X}'.format(*map(int, source_ip))

        dest_ip = Network(private=True).ipv4.split('.')
        dest_ip_hex = '{:02X} {:02X} {:02X} {:02X}'.format(*map(int, dest_ip))

        return ('45'                    #IP version and header length (multiples of 4 bytes)   
                '00'                      
                'XX XX'                 #Length - will be calculated and replaced later
                '00 00'                   
                '40 00 40'                
                '11'                    #Protocol (0x11 = UDP)          
                'YY YY'                 #Checksum - will be calculated and replaced later      
                '{source_ip}'           #Source IP (Default: 127.0.0.1)         
                '{dest_ip}').format(
                    source_ip=source_ip_hex,
                    dest_ip=dest_ip_hex
                )          #Dest IP (Default: 127.0.0.1) 

    

    @property
    def __udp_header(self):
        return ('80 01'                   
                'XX XX'                 #Port - will be replaced later                   
                'YY YY'                 #Length - will be calculated and replaced later        
                '00 00')
                

    def __get_byte_length(self, string1):
        return len(''.join(string1.split())) / 2

    def __write_byte_string_to_file(self, bytestring, filename):
        tmpfile = BytesIO()

        #bitout = open(tmpfile, 'wb')
        for string in bytestring:
            bytelist = string.split()  
            bytes = binascii.a2b_hex(''.join(bytelist))
            tmpfile.write(bytes)
       # bitout.close()
        encoded = base64.b64encode(tmpfile.getvalue())
        return {
            'attachment': {
                'filename': '{}.pcap'.format(filename),
                'base64': encoded
            }
        }
        

    #Calculates and returns the IP checksum based on the given IP Header
    def __ip_checksum(self, iph):
        #split into bytes    
        words = self.__split(''.join(iph.split()),4)
        csum = 0
        for word in words:
            csum += int(word, base=16)

        csum += (csum >> 16)
        csum = csum & 0xFFFF ^ 0xFFFF

        return csum

    #Splits the string into a list of tokens every n characters
    def __split(self, string1, n):
        return [string1[start:start+n] for start in range(0, len(string1), n)]

    def generate(self, message, pcapfile, port=9600):
        count = 0
        bytestring_list = []
        #while count < 10:
        # Replace upd header with desired port
        udp = self.__udp_header.replace('XX XX',"%04x"%port)
        # getting the length of our provided message and the upd header
        udp_len = self.__get_byte_length(message) + self.__get_byte_length(self.__udp_header)
        # replace upd header length with combined message and existing upd header length
        udp = udp.replace('YY YY',"%04x"%udp_len)

        # get upd header legnth and ip header length
        ip_len = udp_len + self.__get_byte_length(self.__ip_header)
        # replace ip header legnth with the combined upd and ip header length
        ip = self.__ip_header.replace('XX XX',"%04x"%ip_len)
        # Clear current ip header checksum and set to 00 00
        checksum = self.__ip_checksum(ip.replace('YY YY','00 00'))
        # replace ip header checksum with generated ip checksum
        ip = ip.replace('YY YY',"%04x"%checksum)
        
        
        pcap_len = ip_len + self.__get_byte_length(self.__ethernet_header)
        hex_str = "%08x"%pcap_len
        reverse_hex_str = hex_str[6:] + hex_str[4:6] + hex_str[2:4] + hex_str[:2]
        pcaph = self.__packet_header.replace('XX XX XX XX',reverse_hex_str)
        pcaph = pcaph.replace('YY YY YY YY',reverse_hex_str)

        bytestring_list.append(self.__global_header + pcaph + self.__ethernet_header + ip + udp + message)
            #count += 1    
        return self.__write_byte_string_to_file(bytestring_list, pcapfile)



pcap = PCAP()

pcap = pcap.generate(__MESSAGE__, 'test_pcap.pcap')

print(pcap)