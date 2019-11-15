import requests, os.path, ast

class Words(object):

    __URL = 'https://random-word-api.herokuapp.com/all?key={my_api_key}'
    __API_KEY = '6G6SW5LH'

    def get(self):
        self.save()
        f = open("words.txt", "r")
        contents = ast.literal_eval(f.read())
        return contents

    def save(self):
        if not os.path.isfile('words.txt'):
            response = requests.get(self.__URL.format(my_api_key=self.__API_KEY))
            response.raise_for_status() # ensure we notice bad responses
            file = open("words.txt", "w")
            file.write(response.content)
            file.close()