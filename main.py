from LexAna import LexicalAnalyser

la = LexicalAnalyser({
    "token"      : r"if|then|else|for|fun|string|number|var",
    "ignored"    : r"[\ |(|;]",
    "literal"    : r"[+|-|*|/|=|==|!=|>|>=|<|<=|(|)|,|;]",
    "string"     : r'\".*?\"|\'.*?\'[;]*',
    "number"     : r'[0-9]+[.]{0,1}[0-9]*[;]*',
    "identefire" : r'[a-zA-Z_][a-zA-Z0-9_]*[;]*',
})

la.parse(r"if (5>10) then print (5) ; alexander = 15")

print(LexicalAnalyser.data)