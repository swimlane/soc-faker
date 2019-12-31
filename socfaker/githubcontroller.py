import os
import yaml
from github import Github

import constants as constants


class GitHubController(object):

    def __init__(self):
        token = self.__get_token_from_config()
        self.github = Github(token)

    def __get_token_from_config(self):
        cfg = ''
      
        filename = os.path.join(constants.__FOLDER_PATH__, constants.__CONFIG_FILE__)
        with open(filename, 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
        if 'GitHub' in cfg:
            if 'token' in cfg['GitHub']:
                return cfg['GitHub']['token']

