def findDivisors(a):
    return [ x for x in range(a/2,0,-1) if a%x==0 ]
