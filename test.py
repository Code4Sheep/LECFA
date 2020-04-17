import math
from coolFuncs import gcd, modInverse, ellipticAddition, Pair, doubleandadd,LECFA,binarray

ans = gcd(15,9)

E = Pair(14,19)

R = Pair(3067,396)
Q = Pair(0,0)



pack = ellipticAddition(Q,R,E,6887)

#if pack.geta() == -1:
#    print(str(pack.getb()) + " is a factor of " + str(187))
#else:
print("P3(" +str(pack.geta()) + "," + str(pack.getb())+")")

print(str(ans))
print(str(-5 % 15))

n = 1
N = 3623
E = Pair(14,19)
P = Pair(6,730)

R = doubleandadd(n,P,E,N)

print("R(" + str(R.geta()) + "," + str(R.getb()) + ")")

d = LECFA(6887)

print(str(d))

a = binarray(2)

#print(a)


a = [[1,2],[2,1]]
a.append([3,3])
print (str(a[2][1]))