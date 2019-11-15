import random, time
import socket
from faker import Faker  # pip install faker
# import string
import decimal
import pendulum  # pip install pendulum
from threading import Thread
from useragent import UserAgent



class Ransomware(Thread):

    def __init__(self, src_ip=None, external_ip=None, external_paths=None):
        super(Ransomware, self).__init__()
        self.log_list = []
        self.fake = Faker('en_US')
        if src_ip:
            self.ip = src_ip
          #  self.syslog = syslog
            self.user_agent = random.choice(UserAgent().get())
            self.generated_logs = 0
           # self.system_type = system_type

       # if self.system_type in ['ransomware']:
        self.external_paths = external_paths
        self.external_ip = external_ip



    def wait(self, min_time=100, max_time=10000):
        time.sleep(float(decimal.Decimal(random.randrange(min_time, max_time))/1000))

    def generate(self, type):
        self.wait()
        self.generateRansomwareTraffic()
        if type == 'clean':
            self.generateRandomTraffic()

        if type == 'ransomware':
            self.generateRandomTraffic()
            self.generateRansomwareTraffic()


    def generateRandomTraffic(self):
        for _ in range(random.randint(10, 150)):
            self.generateWebLog(direction='outbound', src_ip=self.ip, dst_ip=None, method=None, path=None, filename=None, extension=None, response_code=None, user_agent=self.user_agent, referrer=None)
            self.wait(100, 500)

    def generateRansomwareTraffic(self):
        # Initial Infection GET Request (Phishing Email)
        self.generateWebLog(direction='outbound', src_ip=self.ip, dst_ip=self.external_ip, method='GET', path=None, filename=None, extension=random.choice(["exe", "zip", "xlsx", "docx", "docm", "xlsm"]), response_code="200", user_agent=self.user_agent, referrer="-")

        self.wait(10000, 30000)
        # Initial Post-Infection POST Request
        for _ in range(random.randint(2, 5)):
            self.generateWebLog(direction='outbound', src_ip=self.ip, dst_ip=self.external_ip, method='POST', path=random.choice(self.external_paths), filename=None, extension=None, response_code="200", user_agent=self.user_agent, referrer="-")

        self.wait()
        # Secondary Post-Infection Traffic
        for _ in range(random.randint(10, 50)):
            self.generateWebLog(direction='outbound', src_ip=self.ip, dst_ip=None, method='POST', path=random.choice(self.external_paths), filename=None, extension=None, response_code=None, user_agent=self.user_agent, referrer="-")
            self.wait(100, 5000)



    def generateWebLog(self, direction=None, src_ip=None, dst_ip=None, method=None, path=None, filename=None, extension=None, response_code=None, user_agent=None, referrer=None):
        if direction == "outbound":
            if not src_ip:
                src_ip = "10.20.{}.{}".format(random.choice(["10", "20", "30", "40"]), random.randint(1, 254))

            if not dst_ip:
                dst_ip = self.fake.ipv4_public()

        elif direction == "inbound":
            if not src_ip:
                src_ip = self.fake.ipv4_public()

            if not dst_ip:
                dst_ip = "10.20.{}.{}".format(random.choice(["10", "20", "30", "40"]), random.randint(1, 254))

        if not method:
            method = random.choice(["GET"] * 10 + ["POST"] * 5 + ["HEAD"])

        if not path:
            path = self.fake.uri_path(deep=random.randint(0, 6))

        if not filename:
            if not extension:
                if method == "POST":
                    extension = random.choice(["php"] * 10 + ["asp", "exe"])
                else:
                    extension = random.choice(["html", "htm", "gif", "php", "jpg", "png", None])

            if extension:
                filename = self.fake.file_name(extension=extension)
            else:
                filename = self.fake.file_name()

        full_path = "/{}/{}".format(path, filename)

        timestamp = pendulum.now().to_iso8601_string()

        if not user_agent:
            user_agent = random.choice(self.user_agents)

        if not response_code:
            response_code = random.choice(["200"] * 10 + ["404"] * 8 + ["401"] * 2 + ["302"] * 1)

        if response_code == "200":
            duration = "{}".format(random.randint(10000, 60000))  # milliseconds
        else:
            duration = "{}".format(random.randint(100, 12000))

        if not referrer:
            if random.randint(0, 3) == 0:  # make fake referrer
                referrer = self.fake.uri()
            else:
                referrer = "-"

        log = """{timestamp} {src_ip} => {dst_ip} {method} {full_path} {response_code} {duration} {referrer} \"{user_agent}\"""".format(
            timestamp=timestamp,
            src_ip=src_ip,
            dst_ip=dst_ip,
            method=method, 
            full_path=full_path, 
            response_code=response_code, 
            duration=duration,
            referrer=referrer, 
            user_agent=user_agent)

        print(log)
        self.log_list.append(log)

        self.generated_logs += 1


       # self.sendLog(log)