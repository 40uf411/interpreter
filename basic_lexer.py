import re

class LexicalAnaliser(object):
    token = "if|then|else|for|fun|string|number|var"

    ignored = "[ |\t|\n]"

    literals = "[+|-|*|/|=|==|!=|>|>=|<|<=|(|)|,|;]"

    formats = {
        "string" : r'\".*?\"',
        "number" : r'[0-9]*.[0-9]*',
        "identefire" : r'[a-zA-z_][a-zA-z0-9_]*'
    }
    
    @staticmethod
    def match(string):
        if re.compile(LexicalAnaliser.token).fullmatch(string):
            print(string + " is a token\n")

        elif re.compile(LexicalAnaliser.ignored).fullmatch(string):
            print(string + " is an ignored\n")

        elif re.compile(LexicalAnaliser.literals).fullmatch(string):
            print(string + " is a literals\n")

        elif re.compile(LexicalAnaliser.formats['string']).fullmatch(string):
            print(string + " is a string\n")

        elif re.compile(LexicalAnaliser.formats['number']).fullmatch(string):
            print(string + " is a number\n")

        elif re.compile(LexicalAnaliser.formats['identefire']).fullmatch(string):
            print(string + " is a identefire\n")
        
        else:
            print("error: unexpected " + string)

    @staticmethod
    def parse(string):

        str_mode = False
        readed_word = ""

        for letter in string:
            if (not str_mode and letter in [" ", "\t", "\n", ";"] ):
                LexicalAnaliser.match(string = readed_word)
                readed_word = ""
            else:
                readed_word = readed_word +  letter 
                if (letter == '"'):
                    str_mode = not str_mode

        if readed_word is not None:
            LexicalAnaliser.match(string = readed_word)



        
    
LexicalAnaliser.parse(string = "if + hello 8484")