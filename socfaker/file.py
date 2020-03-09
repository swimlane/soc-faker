import random, requests, pendulum, hashlib, string, os, fnmatch

class File(object):

    __DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'filenames'))

    def __init__(self):
        self.__filename = None
        self.__full_path = None
        self._filenames = self.__check_file_directory()
        self._name = ''
        self.random_value = ''.join(random.choice(string.ascii_uppercase) for i in range(256))

    @property
    def filename(self):
        data = None
        file_type = random.choice(['exe', 'sys', 'bin'])
        if not self.__filename:
            for item in self._filenames:
                if file_type in item:
                    with open(item, 'r') as file:
                        data = file.read()
                    return random.choice(data.splitlines()).rsplit('\\',1)[1]
        return self.__filename


    @property
    def full_path(self):
        data = None
        file_type = random.choice(['exe', 'sys', 'bin'])
        if not self.__full_path:
            for item in self._filenames:
                if file_type in item:
                    with open(item, 'r') as file:
                        data = file.read()
                    return random.choice(data.splitlines()).rsplit('\\',1)[0]
        return self.__full_path
           
    @property
    def signed(self):
        return random.choice(['True', 'False'])

    @property
    def signature(self):
        return 'Microsoft Windows'

    @property
    def signature_status(self):
        return random.choice(['Verified', 'Unknown', 'Counterfit'])
        
    @property
    def size(self):
        file_size_list = []
        precision = 2
        size = random.randint(1, 3221225472)
        suffixes=['B','KB','MB','GB','TB']
        suffixIndex = 0
        while size > 1024 and suffixIndex < 4:
            suffixIndex += 1 #increment the index of the suffix
            size = size/1024.0 #apply the division
            file_size_list.append("%.*f%s"%(precision,size,suffixes[suffixIndex]))
        
        return file_size_list

    @property
    def timestamp(self):
        return pendulum.now().subtract(
            years=random.randint(0, 8),
            days=random.randint(1,365),
            hours=random.randint(1,24),
            minutes=random.randint(1, 60), 
            seconds=random.randint(1, 60)
        ).to_datetime_string()

    @property
    def md5(self):
        return random.choice([hashlib.md5(str(self.random_value).encode('utf-8')).hexdigest()])
      
    @property
    def sha1(self):
        return random.choice([hashlib.sha1(str(self.random_value).encode('utf-8')).hexdigest()])
      
    @property
    def sha256(self):
        return random.choice([hashlib.sha256(str(self.random_value).encode('utf-8')).hexdigest()])

    @property
    def hashes(self):
        return {
            'md5': self.md5,
            'sha1': self.sha1,
            'sha256': self.sha256
        }

    def __check_file_directory(self):
        matches = []
        file_path = os.path.abspath(self.__DATA_PATH)
        for root, dirnames, filenames in os.walk(file_path):
            for filename in fnmatch.filter(filenames, '*.txt'):
                matches.append(os.path.abspath(os.path.join(root, filename)))
        return matches