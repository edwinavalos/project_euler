#https://projecteuler.net/problem=6

big=0
sum=0
for i in range(1,101):
    big=big+(i**2)
    sum=sum+i
print (sum**2)-big

