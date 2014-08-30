#https://projecteuler.net/problem=3


def isPrime(x):
    if x==2: return True 
    for i in range(2,int(x**.5)+1):
        if x % i == 0: return False
    else: return True

#print isPrime(7)
#print isPrime(23)
#print isPrime(2)
#print isPrime(10)


a=600851475143
for i in xrange(int(a**.5)+1,0,-2):
    if isPrime(i) and (a % i == 0):
        print i
        break
