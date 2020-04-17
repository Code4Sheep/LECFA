import math

class Pair:
    #   used to model points and curves
    #   useful, generic, possibly confusing
    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)
    def geta(self):
        return self.a
    def getb(self):
        return self.b


def gcd(a,b):
    #recursive gcd func
    if a == 0:
        return b
    gcdpass = gcd(b%a,a)
    return gcdpass


def modInverse(a, m):
    #calcs the modular inverse
    m0 = m
    y = 0
    x = 1
    if (m == 1):
        return 0
    while (a > 1):
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if (x < 0):
        x = x + m0
    return x


def ellipticAddition(P1,P2,E,N):
    #   the work horse, does the addition according to theorm 6.6
    #   actually doesnt check for a - d cases
    if(P1.geta() ==  P2.geta() and P1.getb() ==  P2.getb()):
        top = (3*(P1.geta())*(P1.geta())  + E.geta()) % N
        bot = modInverse((2*P1.getb()),N)
        print(str(top) + " " + str(bot))

    else:
        bot = P2.geta() - P1.geta()
        if (gcd(bot,N) != 1):
            ret = Pair(-1,bot)
            return ret
        bot = modInverse(bot,N)
        top = (P2.getb() - P1.getb()) % N


    lamb = (top * bot) % N
    print("Lamb: " + str(lamb))
    x3 = (lamb*lamb - P1.geta() - P2.geta()) % N
    y3 = (lamb*(P1.geta() - x3) - P1.getb()) % N

    ret = Pair(x3,y3)
    return ret


