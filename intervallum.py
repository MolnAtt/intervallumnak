
class Intervallum:
    def __init__(self, *args):
        if len(args)==1:
            tomb = args[0].split(';')
            self.e = '-' if tomb[0][1:]=='-' else int(tomb[0][1:])
            self.v = '-' if tomb[1][:-1]=='-' else int(tomb[1][:-1])
            self.b = tomb[0][0]=='['
            self.j = tomb[1][-1]==']'
        elif len(args)==4:
            self.b = args[0]
            self.e = args[1]
            self.v = args[2]
            self.j = args[3]
        else:
            print('hibás intervallummegadás, rossz argumentumszám!')
        self.ures = self.e!='-' and self.v!='-' and (self.v < self.e or (self.v == self.e and not self.b and not self.j))

    def __str__(self) -> str:
        return '0' if self.ures else ('[' if self.b else ']') + str(self.e) + ';' + str(self.v) + (']' if self.j else '[')

    def ures(self):
        return  
        
    def korlatossag(self) -> (bool,bool):
        return (self.e=='-', self.v=='-')
        
    def switch(self,melyiket):
        return ']' if (self.b if melyiket=='b' else self.j)=='[' else '[' 

    def komplementerstring(self):
        if self.ures: 
            return set(Intervallum(']-;-['))
        k = self.korlatossag()
        if self.e=='-' and self.v=='-':
            return str(Intervallum('[1;0]'))
        if self.e=='-' and self.v!='-':
            return str(Intervallum(not self.j, self.v, '-', False))
        if self.e!='-' and self.v=='-':
            return str(Intervallum(False, '-', self.e, not self.b))
        return f'{Intervallum(False, "-", self.e, not self.b)} U {Intervallum(not self.j, self.v, "-", False)}'
        

a = Intervallum(']3;5[')
b = Intervallum(']-;5]')
c = Intervallum(']-3;-[')
d = Intervallum(']-;-[')

print(f'{a} komplementere: {a.komplementerstring()}')
print(f'{b} komplementere: {b.komplementerstring()}')
print(f'{c} komplementere: {c.komplementerstring()}')
print(f'{d} komplementere: {d.komplementerstring()}')


