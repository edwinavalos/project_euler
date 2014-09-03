#https://projecteuler.net/problem=21

def findDivisors(a):
    return [ x for x in range(a/2,0,-1) if a%x==0 ]

holder=[]
for a in range(0,10001):
    b=sum(findDivisors(a))
    c=sum(findDivisors(b))
    if a!=b and c==a:
        if [c] and [a] not in holder:
            holder.append(a)
            holder.append(c)
print sum(holder)/2 
