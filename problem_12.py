#https://projecteuler.net/problem=12

def findFactors(x):
    amount=0
    for i in range(1,int(x**.5)+1):
        if x % i == 0:
            amount+=2
    return amount

x=2
while True:
    holder=[]
    for i in range(x):
        holder.append(i)
    cur=sum(holder)
    x+=1
    factors=findFactors(cur)
    if factors % 50 == 0:
        print "{} has {} factors".format(cur,factors)
    if factors > 500:
        print cur
        break
