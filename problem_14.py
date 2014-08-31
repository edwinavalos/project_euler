#https://projecteuler.net/problem=14

def collatz(a):
    if a%2==0:
        a=a/2
    else:
        a=(a*3)+1
    return a

biggest=0
for a in xrange(1,1000000):    
    initial=a
    holder=[a]
    while a!=1:
        a=collatz(a)
        holder.append(a)
    #print holder
    if len(holder)>biggest:
        biggest=len(holder)
        print initial 
print "done"
