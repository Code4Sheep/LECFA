import math
from coolFuncs import gcd, modInverse, ellipticAddition, Pair

ans = gcd(15,9)

E = Pair(3,7)

P1 = Pair(43,126)
P2 = Pair(38,112)



pack = ellipticAddition(P2,P1,E,187)

if pack.geta() == -1:
    print(str(pack.getb()) + " is a factor of " + str(187))
else:
    print("P3(" +str(pack.geta()) + "," + str(pack.getb())+")")

print(str(ans))
print(str(-5 % 15))