import math, random

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

def binarray(X):
    #   converts int to a reversed binary array
    #   Ex. 3 => [0,1,1]
    list = []
    while  X > 0:
        list.append(X%2)
        X = X//2
    return list

def ellipticAddition(P1,P2,E,N):
    #   does the addition according to theorm 6.6
    #   actually doesnt check for a - d cases
    if(P1.geta() ==  P2.geta() and P1.getb() ==  P2.getb()):
        #   P1 == P2
        top = (3*(P1.geta())*(P1.geta())  + E.geta()) % N
        bot = 2*P1.getb() % N
        if (gcd(bot,N) != 1):
            #   check if we can invert bottom
            #   if not return special case
            ret = Pair(-1, bot)
            return ret
        bot = modInverse(bot, N)
    else:
        #   P1 =/= P2
        bot = (P2.geta() - P1.geta())%N
        if (gcd(bot,N) != 1):
            #   check if we can invert bottom
            #   if not return special case
            ret = Pair(-1, bot)
            return ret
        bot = modInverse(bot, N)
        top = (P2.getb() - P1.getb()) % N
    #   Calc the new point
    lamb = (top * bot) % N
    x3 = (lamb*lamb - P1.geta() - P2.geta()) % N
    y3 = (lamb*(P1.geta() - x3) - P1.getb()) % N
    ret = Pair(x3,y3)
    return ret

def LECFA(N):
    # implementation of factorization algorithm
    A = random.randint(1,N-1)
    a = random.randint(1,N-1)
    b = random.randint(1,N-1)
    P = Pair(a,b)
    B = (math.pow(b,2) - math.pow(a,3) - (A*a)) % N
    E = Pair(A,B)
    #   idk what is normal but 100 works
    jmax = 100
    for j in range(2, jmax):
        binlist = binarray(j)
        Q2 = ellipticAddition(P, P, E, N)
        #   Flag notifies if its the first point
        #   being added to Q, kinda jank but works
        flag = 0
        for i in range(0, len(binlist)):
            #   iterrate through the bin array if its a one add into Q
            if binlist[i] == 1:
                if flag == 0:
                    #   first addition case
                    flag = 1
                    if i == 0:
                        Q = P
                    else:
                        #   any number can be express as 2^x + 1
                        #   not the most elegant but it works
                        n = pow(2,i)/2
                        Q = doubleandadd(n, Q2, E, N)
                else:
                    #   just add onto existing Q
                    n = pow(2, i) / 2
                    R = doubleandadd(n, Q2, E, N)
                    Q = ellipticAddition(R, Q, E, N)
        P = Q
        if P.geta() == -1:
            #   check if we have a "fail"
            if 1 < P.getb() < N:
                return gcd((-1 * P.getb()) % N, N)
        if P.getb() == N:
            # -1 is just the fail case
            return -1
        if (j == jmax):
            return -1


def doubleandadd(n,P,E,N):
    #   implementation of algorithm in CH 6.3.1
    Q = P
    R = Pair(0,0)
    watch = 0
    i = 0
    while n > 0:
        if (n % 2 == 1):
            if (watch == 0):
                #   if its the first then equate
                R = Q
                watch = 1
            else:
                R = ellipticAddition(R,Q,E,N)
        Q = ellipticAddition(Q,Q,E,N)
        n = n//2
        i = i+1
    return R









