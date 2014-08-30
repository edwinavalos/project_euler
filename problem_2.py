#https://projecteuler.net/problem=2

col=[]
def fib(prv,cur):
    nxt=prv+cur
    if nxt % 2 == 0: col.append(nxt)
    return cur,nxt 
cur=0
nxt=1
while cur < 4000000:
    cur,nxt=fib(cur,nxt)
print sum(col)
