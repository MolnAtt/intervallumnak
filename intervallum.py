class Intervallum:
    def __init__(self, string):
        tomb = string.split(';')
        self.e = tomb[0][1:]
        self.v = tomb[1][:-1]
        self.b = tomb[0][0]=='['
        self.j = tomb[1][-1]==']'
    
    def __str__(self):
        return ('[' if self.b else ']') + self.e + ';' + self.v + (']' if self.j else '[')

    def __add__(self, other):
        if ()
        
        return 

a = Intervallum('[3;5]')
print(a)
