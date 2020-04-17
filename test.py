import math
from coolFuncs import gcd, modInverse, ellipticAddition, Pair, doubleandadd,LECFA,binarray

ans = gcd(15,9)

E = Pair(1277,279)

R = Pair(3227,5396)
Q = Pair(3642,5642)



pack = ellipticAddition(R,R,E,6887)

#if pack.geta() == -1:
#    print(str(pack.getb()) + " is a factor of " + str(187))
#else:
print("P3(" +str(pack.geta()) + "," + str(pack.getb())+")")
print(str(ans))
print(str(-5 % 15))
n = 947
N = 3623
E = Pair(14,19)
P = Pair(6,730)
R = doubleandadd(n,P,E,N)
print("R(" + str(R.geta()) + "," + str(R.getb()) + ")")
d = LECFA(6887)

print("LECFA: " + str(d))

a = binarray(2)

#print(a)

