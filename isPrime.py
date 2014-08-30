def isPrime(x):
    if x==1: return False
    elif x==2: return True 
    for i in range(2,int(x**.5)+1):
        if x % i == 0: return False
    else: return True

