import re


class LexicalAnalyser(object):
    patterns = {}
    data = []
    
    def __init__(self, patterns):
        self.patterns = patterns
    
    def match(self, word):
        found = False
        for pattern, value in self.patterns.items():
            if re.compile(value).fullmatch(word):
                found = True
                if pattern != "ignore":
                    self.data.append((pattern, word))
                break

        #if not found:
        #    raise Exception("Unknown word : '" + word + "'")

    def parse(self, text):
        str_mode = False
        readed_word = ""
        for letter in text:
            if not str_mode and letter in self.patterns['breakpoint']:
                self.match(word=readed_word)
                self.match(word=letter)
                readed_word = ""
            else:
                readed_word += letter
                if letter == '"':
                    str_mode != str_mode
        if readed_word is not None:
            self.match(word=readed_word)

        return self.data
