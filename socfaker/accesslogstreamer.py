import random, time
from faker import Faker 
import decimal
import pendulum 
from threading import Thread
from .useragent import UserAgent
from .network import Network
from .client import Client


class AccessLogStreamer(Thread):

    def __init__(self):
        super(AccessLogStreamer, self).__init__()
        self.__log_list = []
        self.__log_count = 0
        self.__fake = Faker('en_US')

    def __wait(self, min_time=100, max_time=10000):
        time.sleep(float(decimal.Decimal(random.randrange(min_time, max_time))/1000))

    def generate(self, type='test', count=10, path_file='', clients=0):
        self.__wait()
        if clients > 0:
            client_list = Client().get(clients)
        else:
            client_list = []
        if type == 'clean':
            self.__generate_clean_logs(random.randint(1, int(count)), path_file, client_list)
        elif type == 'test':
            self.__generate_test_logs(random.randint(1,int(count)), path_file, client_list)
        return self.__log_list

    def __generate_clean_logs(self, count, path_file='', client_list=[]):
        for _ in range(int(count)):
            self.__generate_outbound_log(path_file=path_file, client_list=client_list)
            self.__wait(100, 500)

    def __generate_test_logs(self, count, path_file='', client_list=[]):
        for _ in range(int(count)):
            self.__generate_outbound_log(method='GET', extension=random.choice(["exe", "zip", "xlsx", "docx", "docm", "xlsm"]), response_code='200', referrer="-", path_file=path_file, client_list=client_list)
        self.__wait(10000, 30000)
        for _ in range(random.randint(2,5)):
            self.__generate_outbound_log(method='POST', response_code="200",referrer="-", path_file=path_file, client_list=client_list)
            self.__wait(100,300)
            self.__generate_clean_logs(random.randint(5, 15), path_file=path_file, client_list=client_list)
            self.__wait(100,1000)
        self.__wait()
        for _ in range(int(count)):
            self.__generate_outbound_log(method='POST', referrer="-", path_file=path_file, client_list=client_list)
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

    def __get_cloned_path(self, path_file):
        with open(path_file) as f:
            paths = f.read().splitlines()
            path = random.choice(paths)
        return path

    def __get_client_pair(self, client_list):
        return random.choice(list(client_list.items()))  

    def __get_logname(self):
        return random.choice(["-", "-", "-"])

    def __get_username(self):
        return random.choice(["-", "-", "-"])

    def __get_version(self):
        return random.choice(["HTTP/1.1", "HTTP/1.1", "HTTP/1.0"])

    def __get_bytes(self):
        return random.randrange(1,999999)

    def __generate_outbound_log(self, method=None, extension=None, response_code=None, referrer=None, path_file='', client_list=[]):
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

        if path_file:
            full_path = self.__get_cloned_path(path_file)
        else:
            full_path = self.__get_full_path(method=method, extension=extension)

        if client_list:
            src_ip, user_agent = self.__get_client_pair(client_list)
        else:
            src_ip=self.__get_public_ip()
            user_agent = UserAgent().get()

        log = """{src_ip} {logname} {username} {timestamp} \"{method} {full_path} {version}\" {response_code} {bytes} \"{referrer}\" \"{user_agent}\"""".format(
            src_ip=src_ip,
            logname=self.__get_logname(),
            username=self.__get_username(),
            # timestamp=pendulum.now().to_iso8601_string(),
            timestamp=pendulum.now().format("\[DD/MMM/YYYY:HH:mm:ss ZZ\]"),
            method=method,
            full_path=full_path, 
            version=self.__get_version(),
            response_code=response_code, 
            bytes=self.__get_bytes(),
            referrer=referrer, 
            user_agent=user_agent)

        # yield log
        print(log)
        self.__log_list.append(log)
        self.__log_count += 1

    def __generate_inbound_log(self, method=None, extension=None, response_code=None, referrer=None, path_file='', client_list=[]):
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

        if path_file:
            full_path = self.__get_cloned_path()
        else:
            full_path = self.__get_full_path(method=method, extension=extension)

        if client_list:
            src_ip, user_agent = self.__get_client_pair(client_list)
        else:
            src_ip=self.__get_public_ip()
            user_agent = UserAgent().get()

        log = """{src_ip} {logname} {username} {timestamp} \"{method} {full_path} {version}\" {response_code} {bytes} \"{referrer}\" \"{user_agent}\"""".format(
            src_ip=src_ip,
            logname=self.__get_logname(),
            username=self.__get_username(),
            # timestamp=pendulum.now().to_iso8601_string(),
            timestamp=pendulum.now().format("\[DD/MMM/YYYY:HH:mm:ss ZZ\]"),
            method=method,
            full_path=full_path, 
            version=self.__get_version(),
            response_code=response_code, 
            bytes=self.__get_bytes(),
            referrer=referrer, 
            user_agent=user_agent)

        yield log
        self.__log_list.append(log)
        self.__log_count += 1
