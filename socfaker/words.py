import requests, os, ast


class Words(object):

    __DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'words' + '.txt'))
    __WORD_LIST = None
    __URL = 'https://random-word-api.herokuapp.com/all?key={my_api_key}'
    # 'https://raw.githubusercontent.com/elasticdog/genhost/master/wordlist'
    __API_KEY = None

    def get(self):
        word_list = []
        if not self.__WORD_LIST:
            with open(self.__DATA_PATH, 'r') as wordlist:
                for line in wordlist:
                    if line:
                        word_list.append(line.strip('\n'))
                self.__WORD_LIST = word_list
        return self.__WORD_LIST
