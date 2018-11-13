import re

class LexicalAnalyser(object):
    patterns = {}
    data = []
    
    def __init__(self,patterns):
        self.patterns = patterns
    
    def match(self, string):
        for pattern, value in self.patterns.items():
            if re.compile(value).fullmatch(string):
                self.data.append( (string,pattern) )
                break

    def parse(self, string):
        str_mode = False
        readed_word = ""
        for letter in string:
            if (not str_mode and letter in self.patterns['ignored'] ):
                self.match(string = readed_word)
                readed_word = ""
            else:
                readed_word += letter 
                if (letter == '"'):
                    str_mode != str_mode

        if readed_word != None:
            self.match(string = readed_word)
