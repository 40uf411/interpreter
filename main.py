from LexAna import LexicalAnalyser
from SynAna import SyntacticalAnalyser

# our basic language words RE
Lexics = {
    "token"      : r"if|then|else|for|fun|string|number|var",
    "ignore"     : r"[ ]",
    "literal"    : r"[=|==|!=|>|>=|<|<=|(|)|,]",
    "operator"   : r"[+|-|*|/]",
    "string"     : r'\".*?\"|\'.*?\'',
    "number"     : r'[0-9]+[.]{0,1}[0-9]*',
    "identifier" : r'[a-zA-Z_][a-zA-Z0-9_]*',
    # setting break points
    "breakpoint" : "[ |;|+|-|*|/|=|==|!=|>|>=|<|<=|(|)|,|\n]",
}

# our basic rules
Syntax = {
    "affectation" : [("identifier", ""), ("literal", "="), ("number", "")]
}

# our code
code = "x = (a+b);"

# creating our analysers
la = LexicalAnalyser(Lexics)
sa = SyntacticalAnalyser(Syntax)

# processing the data

l_data = la.parse(code)
#s_data = sa.parse(l_data)

# printing the results
print("income code: ", code)
print("lexical array : ", l_data)
#print("syntactic tree", s_data)
