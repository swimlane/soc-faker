import requests, os, ast

class Words(object):

    __DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'words' + '.txt'))
    __WORD_LIST = None
    __URL = 'https://random-word-api.herokuapp.com/all?key={my_api_key}'
    __API_KEY = None

    def get(self):
        word_list = []
        if not self.__WORD_LIST:
            with open(self.__DATA_PATH, 'r') as wordlist:
                for line in wordlist:
                    if line:
                        word_list.append(line)
                self.__WORD_LIST = word_list
        return self.__WORD_LIST

    def get_raw_contents(self):
        raise NotImplementedError
        #response = requests.get(self.__URL.format(my_api_key=self.__API_KEY))
        #response.raise_for_status() # ensure we notice bad responses
        #return response.content

    def save(self):
        raise NotImplementedError
        #if not os.path.isfile('./data/words.txt'):
        #    response = requests.get(self.__URL.format(my_api_key=self.__API_KEY))
        #    response.raise_for_status() # ensure we notice bad responses
        #    file = open("./data/words.txt", "w")
        #    file.write(response.content)
        #    file.close()