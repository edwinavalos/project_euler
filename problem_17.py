#https://projecteuler.net/problem=17

a = {
        "0":
            {
                "1s":"",
                "10s":""
            },
        "1":
            {
                "1s":"one",
                "10s":
                    {
                        "0":"ten",
                        "1":"eleven",
                        "2":"twelve",
                        "3":"thirteen",
                        "4":"fourteen",
                        "5":"fifteen",
                        "6":"sixteen",
                        "7":"seventeen",
                        "8":"eighteen",
                        "9":"nineteen",
                    },
                "100s":"one",
                "1000s":"one"
            },
        "2":
            {
                "1s":"two",
                "10s":"twenty",
                "100s":"two"
            },
        "3":
            {
                "1s":"three",
                "10s":"thirty",
                "100s":"three"
            },
        "4":
            {
                "1s":"four",
                "10s":"forty",
                "100s":"four"
            },
        "5":
            {
                "1s":"five",
                "10s":"fifty",
                "100s":"five"
            },
        "6":
            {
                "1s":"six",
                "10s":"sixty",
                "100s":"six"
            },
        "7":
            {
                "1s":"seven",
                "10s":"seventy",
                "100s":"seven"
            },
        "8":
            {
                "1s":"eight",
                "10s":"eighty",
                "100s":"eight"
            },
        "9":
            {
                "1s":"nine",
                "10s":"ninety",
                "100s":"nine"
            }
    }
def makeWords(number):
    number=str(number)
    if len(number)==1:
        words=""
        ones=number[0]
        words+=a[ones]["1s"]
    if len(number)==2:
        words=""
        tens=number[0]
        ones=number[1]
        if tens=="1":
            words+=a[tens]["10s"][ones]
        else:
            words+=a[tens]["10s"]
            words+=" "
            ones=number[1]
            words+=a[ones]["1s"]
    if len(number)==3:
        words=""
        hundreds=number[0]
        tens=number[1]
        ones=number[2]
        words+=a[hundreds]["100s"]
        if tens=="0" and ones=="0":
            words+=" hundred "
        else:
            words+=" hundred and "
        if tens=="1":
            words+=a[tens]["10s"][ones]
        else:
            tens=number[1]
            words+=a[tens]["10s"]
            words+=" "
            ones=number[2]
            words+=a[ones]["1s"]
    if len(number)==4:
        words=""
        thousands=number[0]
        words+=a[thousands]["1000s"]
        words+=" thousand "
    print words
    return len(words.replace(" ",""))

holder=[]
for i in range(1,1001):
    holder.append(makeWords(i))
print sum(holder)
