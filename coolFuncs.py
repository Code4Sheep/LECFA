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

        #i have no idea why but it fixes the problem
        # if (m == 0):
        #     print("black magic")
        #     return -1
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
    list = []
    while  X > 0:
        #print("go")
        list.append(X%2)
        X = X//2

    return list

def ellipticAddition(P1,P2,E,N):
    #   does the addition according to theorm 6.6
    #   actually doesnt check for a - d cases
    if(P1.geta() ==  P2.geta() and P1.getb() ==  P2.getb()):
        top = (3*(P1.geta())*(P1.geta())  + E.geta()) % N
        #print("look")
        bot = 2*P1.getb() % N
        if (gcd(bot,N) != 1):
            ret = Pair(-1,bot)
            return ret
        bot = modInverse(bot,N)

        #print(str(top) + " " + str(bot))

    else:
        bot = (P2.geta() - P1.geta())%N
        if (gcd(bot,N) != 1):
            ret = Pair(-1,bot)
            return ret
        bot = modInverse(bot,N)
        top = (P2.getb() - P1.getb()) % N


    lamb = (top * bot) % N
    #print("Lamb: " + str(lamb))
    x3 = (lamb*lamb - P1.geta() - P2.geta()) % N
    y3 = (lamb*(P1.geta() - x3) - P1.getb()) % N

    ret = Pair(x3,y3)
    return ret

def LECFA(N):
    #random.randint(1,N-1)
    A = random.randint(1,N-1)
    a = random.randint(1,N-1)
    b = random.randint(1,N-1)
    P = Pair(a,b)
    B = (math.pow(b,2) - math.pow(a,3) - (A*a)) % N
    print("B: " + str(B) + " " + str(A))
    E = Pair(A,B)
    jmax = 100
    for j in range (2,jmax):
    #
    #    for i in range(2,j+1):
    #        if (i == 2):
    #            Q = ellipticAddition(P,P,E,N)
    #        else:
    #            tempQ = ellipticAddition(Q,P,E,N)
    #            if (tempQ.geta() == -1 and tempQ.getb() < 0):
    #                Q = ellipticAddition(P,Q,E,N)
    #            else:
    #                Q = tempQ
    #            if (Q.geta() == -1):
    #                if (N > Q.getb() > 0):
    #                    return Q.getb()
    #                else:
    #                    return -1
        binlist = binarray(j)
        print(str(binlist))
        jbreak = []
        Q2 = ellipticAddition(P,P,E,N)
        print(" | Q2: (" + str(Q2.geta()) + "," + str(Q2.getb()) + ")" )
        flag =0
        for i in range(0,len(binlist)):
            if binlist[i] == 1:
                if flag == 0:
                    flag = 1
                    if i == 0:
                        Q = P
                    else:
                        n = pow(2,i)/2
                        print(str(n))
                        Q = doubleandadd(n,Q2,E,N)
                else:
                    n = pow(2, i) / 2
                    #print(str(n))
                    R = doubleandadd(n, Q2, E, N)
                    if R.geta() == -1:
                        if 1 < R.getb() < N:
                            return gcd((-1 * R.getb()) % N, N)
                        if R.getb() == N:
                            return -1
                    #print("R: (" + str(R.geta()) + "," + str(R.getb()) + ")")
                    Q = ellipticAddition(R,Q,E,N)


        #print(" | Q: (" + str(Q.geta()) + "," + str(Q.getb()) + ")")
        P = Q
        print("j: " + str(j)+ " | P: (" + str(P.geta()) + "," + str(P.getb()) + ")" )
        if P.geta() == -1:
            if 1 < P.getb() < N:
                return gcd((-1 * P.getb()) % N, N)
        if P.getb() == N:
            return -1
        if (j == jmax):
            return -1







def doubleandadd(n,P,E,N):
    Q = P
    R = Pair(0,0)
    watch = 0
    i = 0
    while n > 0:
        if (n % 2 == 1):
            if (watch == 0):
                R = Q
                watch = 1
                #print("flipped")
            else:
                R = ellipticAddition(R,Q,E,N)
                #print("~Q: (" + str(Q.geta()) + "," + str(Q.getb()) + ") | R: (" + str(R.geta()) + "," + str(R.getb())+")")
        Q = ellipticAddition(Q,Q,E,N)
        n = n//2
        i = i+1
        #print("i: " + str(i) + " | n: " + str(n) + " | Q: (" + str(Q.geta()) + "," + str(Q.getb()) + ") | R: (" + str(
        #    R.geta()) + "," + str(R.getb())+")")
    return R









