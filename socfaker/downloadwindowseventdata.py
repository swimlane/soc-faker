import requests, yaml, base64, os
from github import Github

from githubcontroller import GitHubController



class DownloadWindowsEventData(GitHubController):

    __RAW_URL = 'https://raw.githubusercontent.com/hunters-forge/OSSEM/master/{}'
    __REPO = 'hunters-forge/OSSEM'

    def __init__(self):
        super(DownloadWindowsEventData, self).__init__()
        self.session = requests.Session()
        self._dataset = []

    def save(self, folder_path):
        repo = self.github.get_repo(self.__REPO)
        contents = repo.get_contents("")
        while contents:
            file_content = contents.pop(0)
            if file_content.type == "dir":
                contents.extend(repo.get_contents(file_content.path))
            else:
                if file_content.path.endswith('md'):
                    if 'windows/security/events' in file_content.path:
                        file_name = '{}{}'.format(folder_path, file_content.path.rsplit('/',1)[1])
                        if not os.path.exists(os.path.dirname(file_name)):
                            os.makedirs(os.path.dirname(file_name))
                            
                        content = self.__download_raw_content(self.__RAW_URL.format(file_content.path))
                        with open('{}{}'.format(folder_path, file_content.path.rsplit('/',1)[1]), 'w+') as f:
                            f.write(content)
                            f.close()
                        
    def __download_raw_content(self, url):
        response = self.session.get(url)
        if response.status_code == 200:
            return response.content
