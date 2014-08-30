#https://projecteuler.net/problem=4
holder=[]
for i in range(1000,100,-1):
    for x in range(1000,100,-1):
        if str(i*x) == str(i*x)[::-1]: 
            holder.append(i*x)
            break
holder.sort()
print holder.pop()
