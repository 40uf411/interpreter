import re

class LexicalAnaliser(object):
    
    token = r"if|then|else|for|fun|string|number|var"

    ignored = r"[\ |\t|\n]"

    literal = r"[+|-|*|/|=|==|!=|>|>=|<|<=|(|)|,|;]"

    formats = {
        "string" : r'\".*?\"|\'.*?\'[;]*',
        "number" : r'[0-9]+[.]{0,1}[0-9]*[;]*',
        "identefire" : r'[a-zA-Z_][a-zA-Z0-9_]*[;]*'
    }
    
    data = []
    
    #@staticmethod
    def match(self, string):

        if re.compile(self.token).fullmatch(string):
            self.data.append( (string,"token") )

        elif re.fullmatch(LexicalAnaliser.ignored, string):
            self.data.append( (string,"ignored") )

        elif re.compile(LexicalAnaliser.literal).fullmatch(string):
            self.data.append( (string,"literal") )

        elif re.compile(self.formats['string']).fullmatch(string):
            self.data.append( (string,"string") )

        elif re.compile(self.formats['number']).fullmatch(string):
            self.data.append( (string,"number") )

        elif re.compile(self.formats['identefire']).fullmatch(string):
            self.data.append( (string,"identefire") )
        
        else:
            exit("error: unexpected " + string)


    #@staticmethod
    def parse(self, string):

        str_mode = False
        readed_word = ""

        for letter in string:

            if (not str_mode and letter in [" ", "\t", "\n"] ):
                self.match(string = readed_word)
                readed_word = ""
            else:
                readed_word += letter 
                if (letter == '"'):
                    str_mode != str_mode

        if readed_word != None:
            self.match(string = readed_word)


la = LexicalAnaliser()

la.parse(string = r"var x = 15;")

print(LexicalAnaliser.data)