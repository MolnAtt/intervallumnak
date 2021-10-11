class Potty:
    def __init__(self, p, t):
        self.poz = p
        self.teli = t
    
    """
    A hatar(False) azt jelzi, hogy a pöttytől balra van az intervallum, 
    a hatar(True) pedig azt jelzi, hogy a pöttytől jobbra van az intervallum.
    """
    def hatar(self,b) -> str: 
        if b:
            return ('[' if self.teli else ']') + str(self.poz) + ';'
        elif 
            return ';' + self.poz + (']' if self.teli else '[')
    
    def komp(self) -> Potty:
        return Potty(self.poz, not self.t)
    
class UDI(): # union of disjoint intervals
    def __init__(self, b, l):
        self.b = b
        self.l = l.copy()

    def __str__(self) -> str:
        if len(self.l) == 1:
            return (']-' + self.hatar(self.b)) if self.b else (self.hatar(self.b) + '-[')
        if len(self.l) == 2:
            if self.b:
                pass
