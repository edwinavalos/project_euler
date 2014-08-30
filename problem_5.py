#https://projecteuler.net/problem=5
x=20
while True:
    check=True
    if x % 1000 == 0:
        print x
    for item in range(1,21):
        if x % item != 0:
            check=False
    if check==True:
        print x
        break
    else:
         x+=1

