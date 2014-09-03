#https://projecteuler.net/problem=24

import itertools

holder=[]
for item in itertools.permutations("0123456789",10):
    holder.append("".join(item))
holder=sorted(holder)
print holder[999999]
