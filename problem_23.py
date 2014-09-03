#https://projecteuler.net/problem=23
from findDivisors import findDivisors

limit=28123
abundant=[]
for number in range(0,limit):
    if sum(findDivisors(number)) > number:
        abundant.append(number)

remove=[False]*(limit+1)

for i in range(len(abundant)):
    for x in range(i,len(abundant)):
        if abundant[i]+abundant[x] <= limit:
            remove[abundant[i]+abundant[x]]=True
        else:
            break

sum=0
for i in range(0,limit):
    if remove[i] == False:
        sum+=i
print sum
