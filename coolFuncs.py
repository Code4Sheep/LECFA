import math

class Point:
    #   just a point
    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)
    def geta(self):
        return self.a
    def getb(self):
        return self.b

def gcd(a,b,x,y):
    if a == 0:
        x = 0
        y = 1
        return b
    tempx = 0
    tempy = 0
    gcdpass = gcd(b%a,a,tempx,tempy)

    x = tempy - (b/a) * tempx
    y = tempx

    return gcdpass

def ellipticAddition(P1,P2):
    if(P1.geta() ==  P2.geta() and P1.geta() ==  P2.geta())
        pass