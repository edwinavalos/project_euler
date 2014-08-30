#https://projecteuler.net/problem=7


def isPrime(x):
    if x==2: return True 
    for i in range(2,int(x**.5)+1):
        if x % i == 0: return False
    else: return True
x = 2
holder=[]
while True:
    if isPrime(x):
        holder.append(x)
    if len(holder)==10002:
        print holder.pop()
        break
    x+=1
print holder
