import random, time
import socket
from faker import Faker 
import decimal
import pendulum 
from threading import Thread
from .useragent import UserAgent
from .network import Network


class LogStreamer(Thread):

    """The LogStreamer class will generate and stream logs in syslog format
    """

    def __init__(self):
        super(LogStreamer, self).__init__()
        self.__log_list = []
        self.__log_count = 0
        self.__fake = Faker('en_US')

    def __wait(self, min_time=100, max_time=10000):
        time.sleep(float(decimal.Decimal(random.randrange(min_time, max_time))/1000))

    def generate(self, type='clean', count=10):
        """Generates either clean syslogs or sprinkles ransomware communications through out the log stream

        Args:
            type (str, optional): The type of logs to generate.  Options are ransomware or clean. Defaults to 'clean'.
            count (int, optional): How many log events are generated. Defaults to 10.

        Returns:
            list: Returns a list of syslog events
        """
        self.__wait()
        if type == 'clean':
            self.__generate_clean_logs(random.randint(1, int(count)))
        elif type == 'ransomware':
            self.__generate_ransomware_logs(random.randint(1,int(count)))
        return self.__log_list

    def __generate_clean_logs(self, count):
        for _ in range(int(count)):
            self.__generate_outbound_log()
            self.__wait(100, 500)

    def __generate_ransomware_logs(self, count):
        for _ in range(int(count)):
            self.__generate_outbound_log(method='GET', extension=random.choice(["exe", "zip", "xlsx", "docx", "docm", "xlsm"]), response_code='200', referrer="-")
        self.__wait(10000, 30000)
        for _ in range(random.randint(2,5)):
            self.__generate_outbound_log(method='POST', response_code="200",referrer="-")
            self.__wait(100,300)
            self.__generate_clean_logs(random.randint(5, 15))
            self.__wait(100,1000)
        self.__wait()
        for _ in range(int(count)):
            self.__generate_outbound_log(method='POST', referrer="-")
            self.__wait(100,5000)

    def __get_method(self):
        return random.choice(["GET"] * 10 + ["POST"] * 5 + ["HEAD"])

    def __get_web_extension(self, method):
        if method == "POST":
            return random.choice(["php"] * 10 + ["asp", "exe"])
        else:
            return random.choice(["html", "htm", "gif", "php", "jpg", "png", None])
            
    def __get_private_ip(self):
        return Network(private=True).ipv4

    def __get_public_ip(self):
        return Network().ipv4

    def __get_full_path(self, method=None, extension=None):
        path = self.__fake.uri_path(deep=random.randint(0, 6))
        if not extension:
            extension = self.__get_web_extension(method)
        filename = self.__fake.file_name(extension=extension)
        return "/{}/{}".format(path, filename)

    def __generate_outbound_log(self, method=None, extension=None, response_code=None, referrer=None):
        if not method:
            method = self.__get_method()
        if not extension:
            extension = self.__get_web_extension(method)
        if not response_code:
            response_code = random.choice(["200"] * 10 + ["404"] * 8 + ["401"] * 2 + ["302"] * 1)

        duration = None
        if response_code == "200":
            duration = "{}".format(random.randint(10000, 60000))  # milliseconds
        else:
            duration = "{}".format(random.randint(100, 12000))

        if not referrer:
            if random.randint(0, 3) == 0:  # make fake referrer
                referrer = self.__fake.uri()
            else:
                referrer = "-"
            
        log = """{timestamp} {src_ip} => {dst_ip} {method} {full_path} {response_code} {duration} {referrer} \"{user_agent}\"""".format(
            timestamp=pendulum.now().to_iso8601_string(),
            src_ip=self.__get_private_ip(),
            dst_ip=self.__get_public_ip(),
            method=method, 
            full_path=self.__get_full_path(method=method, extension=extension), 
            response_code=response_code, 
            duration=duration,
            referrer=referrer, 
            user_agent=UserAgent().get())

       # yield log
        print(log)
        self.__log_list.append(log)
        self.__log_count += 1

        
    def __generate_inbound_log(self, method=None, extension=None, response_code=None, referrer=None):
        if not method:
            method = self.__get_method()
        if not extension:
            extension = self.__get_web_extension(method)
        if not response_code:
            response_code = random.choice(["200"] * 10 + ["404"] * 8 + ["401"] * 2 + ["302"] * 1)

        duration = None
        if response_code == "200":
            duration = "{}".format(random.randint(10000, 60000))  # milliseconds
        else:
            duration = "{}".format(random.randint(100, 12000))

        if not referrer:
            if random.randint(0, 3) == 0:  # make fake referrer
                referrer = self.__fake.uri()
            else:
                referrer = "-"
            
        log = """{timestamp} {src_ip} => {dst_ip} {method} {full_path} {response_code} {duration} {referrer} \"{user_agent}\"""".format(
            timestamp=pendulum.now().to_iso8601_string(),
            src_ip=self.__get_public_ip(),
            dst_ip=self.__get_private_ip(),
            method=method, 
            full_path=self.__get_full_path(method=method, extension=extension), 
            response_code=response_code, 
            duration=duration,
            referrer=referrer, 
            user_agent=UserAgent().get())

        yield log
        self.__log_list.append(log)
        self.__log_count += 1
