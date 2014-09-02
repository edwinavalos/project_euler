#https://projecteuler.net/problem=19

days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
date=["Tuesday",1,"Jan",1901,30]
counter=0
while date[1:4] != [31,"Dec",2000]:
    if date[0:2]==["Sunday",1]:
        counter+=1
    if date[1:3]==[31,"Dec"]:
        date[3]+=1
    if date[1]==date[4]:
        date[1]=1
        date[2]=months[(months.index(date[2])+1)%12]
    else:
        date[1]+=1
    date[0]=days[(days.index(date[0])+1)%7]
    if date[2] in ["Jan","Mar","May","Jul","Aug","Oct","Dec"]:
        date[4]=31
    if date[2] in ["Feb"]:
        if date[3] % 4 == 0 and date[3] != 1900:
                date[4]=29
        elif date[3]==2000:
            date[4]=29
        else:
            date[4]=28
    if date[2] in ["Apr","Jun","Sep","Nov"]:
        date[4]=30
print date
print counter
