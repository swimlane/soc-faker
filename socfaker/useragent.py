import json, requests, datetime, random
from bs4 import BeautifulSoup

__USER_AGENT_PATH__ = './data/useragent.json'
__USER_AGENT_URL__ = 'http://www.useragentstring.com/pages/useragentstring.php?name={}'


class UserAgent(object):

    BROWSER_LIST = ['Firefox','Internet+Explorer','Opera','Safari','Chrome','Edge','Android+Webkit+Browser']

    def __init__(self, force=False):
        self._user_agents = {}
        
        if not self.strings:
            self.download()
        elif self.updated >= (datetime.datetime.now() + datetime.timedelta(hours=1)).isoformat():
                self.download()

        if force:
            self.download()

    def get(self):
        user_agent_list = []
        for key,val in self.strings.iteritems():
            if isinstance(val, list):
                for ua_string in val:
                    user_agent_list.append(ua_string)
        return random.choice(user_agent_list)

    @property
    def updated(self):
        with open(__USER_AGENT_PATH__) as json_file:
            last_updated = json.load(json_file)['updated']
            return last_updated

    @updated.setter
    def updated(self, value):
        with open(__USER_AGENT_PATH__, "w") as f:
            json.dump(value, f)

    @property 
    def strings(self):
        try:    
            with open(__USER_AGENT_PATH__, 'r') as f:
                return json.loads(f.read())
        except:
            return False

    @strings.setter
    def strings(self, value):
        self.download()

    def _download_user_agent_lists(self):
        for browser in self.BROWSER_LIST:
            try:
                with requests.Session() as s:
                    user_agent_list = []
                    download = s.get(__USER_AGENT_URL__.format(browser))
                    if download.status_code == 200:
                        decoded_content = download.content.decode('utf-8', errors='ignore')
                        soup = BeautifulSoup(decoded_content,'html.parser')
                        div = soup.find('div',{'id':'liste'})
                        lnk = div.findAll('a')
                        for link in lnk:
                            try:
                                user_agent_list.append(link.text)
                            except:
                                pass
                    self._user_agents[browser] = user_agent_list
            except:
                pass

    def download(self):
        self._user_agents['updated'] = datetime.datetime.now().isoformat()
        self._download_user_agent_lists()
        self.updated = self._user_agents