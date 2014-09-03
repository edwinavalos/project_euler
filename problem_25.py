#https://projecteuler.net/problem=25

def fib():
    a,b=1,1
    while True:
        yield a
        a,b=b,a+b
f=fib()
counter=0
while True:
    counter+=1
    a=str(f.next())
    if len(a)==1000:
        print counter
        break
