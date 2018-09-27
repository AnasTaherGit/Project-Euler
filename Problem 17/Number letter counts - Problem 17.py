from os import system

def unity(x):
    if x=="1":
        return "one"
    elif x=="2":
        return "two"
    elif x=="3":
        return "three"
    elif x=="4":
        return "four"
    elif x=="5":
        return "five"
    elif x=="6":
        return "six"
    elif x=="7":
        return "seven"
    elif x=="8":
        return "eight"
    elif x=="9":
        return "nine" 
def dizaine(x):
    if x[0]=='0':
        return unity(x[1])
    if x[0]=="1":
        if x[1]=="0":
            return "ten"
        elif x[1]=="1":
            return "eleven"
        elif x[1]=="2":
            return "twelve"
        elif x[1]=="3":
            return "thirteen"
        elif x[1]=="4":
            return "fourteen"
        elif x[1]=="5":
            return "fifteen"
        elif x[1]=="6":
            return "sixteen"
        elif x[1]=="7":
            return "seventeen"
        elif x[1]=="8":
            return "eighteen"
        elif x[1]=="9":
            return "nineteen"
    elif x[0]=="2":
        if x[1]=="0":
            return "twenty"
        else :
            q="twenty"+unity(x[1])
            return q
    elif x[0]=="2":
        if x[1]=="0":
            return "twenty"
        else :
            q="twenty"+unity(x[1])
            return q
    elif x[0]=="3":
        if x[1]=="0":
            return "thirty"
        else :
            q="thirty"+unity(x[1])
            return q
    elif x[0]=="4":
        if x[1]=="0":
            return "forty"
        else :
            q="forty"+unity(x[1])
            return q
    elif x[0]=="5":
        if x[1]=="0":
            return "fifty"
        else :
            q="fifty"+unity(x[1])
            return q
    elif x[0]=="6":
        if x[1]=="0":
            return "sixty"
        else :
            q="sixty"+unity(x[1])
            return q
    elif x[0]=="7":
        if x[1]=="0":
            return "seventy"
        else :
            q="seventy"+unity(x[1])
            return q
    elif x[0]=="8":
        if x[1]=="0":
            return "eighty"
        else :
            q="eighty"+unity(x[1])
            return q
    elif x[0]=="9":
        if x[1]=="0":
            return "ninety"
        else :
            q="ninety"+unity(x[1])
            return q

def centaine(x):
    if x[1:3]=="00":
        return unity(x[0])+"hundred"
    else :
        b=x[1:3]
        q=unity(x[0])+"hundredand"+dizaine(b)
        return q

S=0
for i in range(1,1001):
    x=str(i)
    if len(x)==1:
        S=S+len(unity(x))
    elif len(x)==2:
        S=S+len(dizaine(x))
    elif len(x)==3:
        S=S+len(centaine(x))
    else :
        S=S+11
print(S)

system("pause")

        
