#https://projecteuler.net/problem=20
import math
bigthing=str(math.factorial(100))
sum=0
for item in bigthing:
    sum+=int(item)

print sum

