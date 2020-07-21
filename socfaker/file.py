import hashlib, string, os, fnmatch
import csv
from .baseclass import BaseClass
from .timestamp import Timestamp


class File(BaseClass):
    """The File class contains properties related to a single file instance

    Returns:
        File: Returns a file object with properties commonly found on files
    """

    __DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'filenames'))
    __MIME_TYPE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'mime_types.csv'))
    _filename_list = []
    _extension = None
    _full_path = None
    _mime_types = []

    def __init__(self):
        super(File, self).__init__()
        self.random_value = ''.join(self.random.choice(string.ascii_uppercase) for i in range(256))

    def __generate_filename_list(self):
        return_list = []
        for root, dirnmaes, filenames in os.walk(self.__DATA_PATH):
            for filename in fnmatch.filter(filenames, '*.txt'):
                filename_list = []
                with open(os.path.join(self.__DATA_PATH, filename), 'r') as file:
                        data = file.read()
                        filename_list = data.splitlines()
                return_list.append({
                    filename: filename_list
                })
        return return_list

    @property
    def name(self):
        """The name of a file

        Returns:
            str: A randomly selected file name
        """
        return self.full_path.rsplit('\\',1)[1]

    @property
    def full_path(self):
        """The full path of a file

        Returns:
            str: A randomly selected file name path
        """
        if not self._filename_list:
            self._filename_list = self.__generate_filename_list()
        if not self._full_path:
            for item in self._filename_list:
                for keys in item.keys():
                    if self.extension in keys:
                        self._full_path = self.random.choice(item[keys])
        return self._full_path

    @property
    def extension(self):
        """The extension of a file

        Returns:
            str: The extension of a file
        """
        if not self._extension:
            self._extension = self.random.choice(['exe', 'sys', 'bin'])
        return self._extension

    @property
    def directory(self):
        """The directory of a file

        Returns:
            str: The directory of a file
        """
        return self.full_path.split('\\',1)[0]

    @property
    def drive_letter(self):
        """The drive letter of a file

        Returns:
            str: A randomly selected drive letter of a file
        """
        return self.random.choice(['C', 'D', 'E', 'Z', 'X'])

    @property
    def gid(self):
        """The GID of a file

        Returns:
            str: A randomly generated GID of a file
        """
        return self.random.randint(100,5000)

    @property
    def type(self):
        """The type of a file

        Returns:
            str: A randomly selected file type
        """
        return self.random.choice([
            'file',
            'dir',
            'symlink'
        ])

    @property
    def mime_type(self):
        """The mime type of a file

        Returns:
            str: A randomly selected file mime type
        """
        if not self._mime_types:
            with open(self.__MIME_TYPE_PATH, 'r') as f:
                csv_reader = csv.reader(f, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        line_count += 1
                    else:
                        self._mime_types.append(row[0])
        return self.random.choice(self._mime_types)

    @property
    def signed(self):
        """Whether the file is signed or not

        Returns:
            str: Returns whether a file is signed or not
        """
        return self.random.choice(['True', 'False'])

    @property
    def signature(self):
        """The file signature

        Returns:
            str: Returns the signature name of Microsoft Windows
        """
        return 'Microsoft Windows'

    @property
    def signature_status(self):
        """The signature status of a file

        Returns:
            str: A randomly selected signature status of Verified, Unknown, or Counterfit
        """
        return self.random.choice(['Verified', 'Unknown', 'Counterfit'])
        
    @property
    def size(self):
        """The file size

        Returns:
            str: A randomly generated file size
        """
        file_size_list = []
        precision = 2
        size = self.random.randint(1, 3221225472)
        suffixes=['B','KB','MB','GB','TB']
        suffixIndex = 0
        while size > 1024 and suffixIndex < 4:
            suffixIndex += 1 #increment the index of the suffix
            size = size/1024.0 #apply the division
            file_size_list.append("%.*f{}".format((precision,size,suffixes[suffixIndex])))
        return file_size_list

    @property
    def timestamp(self):
        """The timestamp of a file in the past

        Returns:
            str: A randomly generated file timestamp is ISO 8601 format
        """
        return Timestamp().in_the_past(
            years=self.random.randint(0, 8),
            days=self.random.randint(1,365),
            hours=self.random.randint(1,24),
            minutes=self.random.randint(1, 60), 
            seconds=self.random.randint(1, 60)
        )
    
    @property
    def accessed_timestamp(self):
        """The last accessed timestamp of a file in the past

        Returns:
            str: A randomly generated accessed timestamp is ISO 8601 format
        """
        return Timestamp().in_the_past(
            days=self.random.randint(1,14),
            hours=self.random.randint(1,24),
            minutes=self.random.randint(1, 60), 
            seconds=self.random.randint(1, 60)
        )

    @property
    def attributes(self):
        """Attributes of the file 

        Returns:
            list: A randomly selected list of file attributes
        """
        return_list = []
        for i in range(self.random.randint(1,5)):
            return_list.append(self.random.choice([
                'archive', 
                'compressed', 
                'directory', 
                'encrypted', 
                'execute', 
                'hidden', 
                'read', 
                'readonly', 
                'system', 
                'write'
            ]))
        return return_list

    @property
    def md5(self):
        """A random generated MD5 hash

        Returns:
            str: A randomly generated MD5 file hash
        """
        return self.random.choice([hashlib.md5(str(self.random_value).encode('utf-8')).hexdigest()])
      
    @property
    def sha1(self):
        """A random generated SHA1 hash

        Returns:
            str: A randomly generated SHA1 file hash
        """
        return self.random.choice([hashlib.sha1(str(self.random_value).encode('utf-8')).hexdigest()])
      
    @property
    def sha256(self):
        """A random generated SHA256 hash

        Returns:
            str: A randomly generated SHA256 file hash
        """
        return self.random.choice([hashlib.sha256(str(self.random_value).encode('utf-8')).hexdigest()])

    @property
    def hashes(self):
        """A dict containing MD5, SHA1, and SHA256 hashes

        Returns:
            str: A randomly generated dict containing MD5, SHA1, and SHA256 hashes
        """
        return {
            'md5': self.md5,
            'sha1': self.sha1,
            'sha256': self.sha256
        }

    @property
    def version(self):
        """A random generated file version string

        Returns:
            str: A randomly generated file version string
        """ 
        return '{}.{}.{}.{}'.format(
            self.random.randint(0,9),
            self.random.randint(0,9),
            self.random.randint(1000,9999),
            self.random.randint(10000,100000),
        )

    @property
    def build_version(self):
        """A build version of a file

        Returns:
            str: Returns the last digit in the version string
        """ 
        return self.version.rsplit('.',1)[1]

    @property
    def checksum(self):
        """A MD5 checksum of a file

        Returns:
            str: Returns a MD5 of the file
        """ 
        return self.md5

    @property
    def install_scope(self):
        """The install scope of a file

        Returns:
            str: Returns a random install scope of user-local or global for a file
        """ 
        return self.random.choice([
            'user-local',
            'global'
        ])
