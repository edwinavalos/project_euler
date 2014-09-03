#https://projecteuler.net/project/resources/p022_names.txt

import ast

values={
        "A":1,
        "B":2,
        "C":3,
        "D":4,
        "E":5,
        "F":6,
        "G":7,
        "H":8,
        "I":9,
        "J":10,
        "K":11,
        "L":12,
        "M":13,
        "N":14,
        "O":15,
        "P":16,
        "Q":17,
        "R":18,
        "S":19,
        "T":20,
        "U":21,
        "V":22,
        "W":23,
        "X":24,
        "Y":25,
        "Z":26
}

with open("names.txt","r") as f:
    a=f.read()
a=ast.literal_eval(a)
a=sorted(a)
bigsum=0
for i in range(len(a)):
    smallsum=0
    for char in a[i]:
        smallsum+=values[char]
    bigsum+=(i+1)*smallsum
    if a[i]=="COLIN":
        print smallsum
        print i+1
print bigsum
