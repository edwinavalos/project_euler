#https://projecteuler.net/problem=3
#I want to see all the primes in the range...

def isPrime(x):
    if x==2: return True 
    for i in range(2,int(x**.5)+1):
        if x % i == 0: return False
    else: return True

print isPrime(7)
print isPrime(23)
print isPrime(2)
print isPrime(10)


a=600851475143

print [ x for x in xrange(int(a**.5)+1,0,-2) if isPrime(x) ]
