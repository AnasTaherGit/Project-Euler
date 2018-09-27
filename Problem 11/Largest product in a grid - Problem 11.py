from random import randint
from os import system

with open("Annexe - Problem 11.txt") as f:
    D=f.read().split()
def conv(x):
    k=int(x)
    return k
D=list(map(conv,D))
All=[]
for i in range(400):
    P=[]
#------- Parcours en ligne ------------    
    try:
        a=D[i]*D[i+1]*D[i+2]*D[i+3]
        P.append(a)
    except IndexError :
        pass
    try:
        a=D[i]*D[i-1]*D[i-2]*D[i-3]
        P.append(a)
    except IndexError :
        pass
    try:
        a=D[i]*D[i+20]*D[i+40]*D[i+60]
        P.append(a)
    except IndexError :
        pass
    try:
        a=D[i]*D[i-20]*D[i-40]*D[i-60]
        P.append(a)
    except IndexError :
        pass
#------- Parcours en diagonale --------
    try:
        a=D[i]*D[i+21]*D[i+42]*D[i+64]
        P.append(a)
    except IndexError :
        pass
    try:
        a=D[i]*D[i-21]*D[i-42]*D[i-64]
        P.append(a)
    except IndexError :
        pass
    try:
        a=D[i]*D[i+19]*D[i+38]*D[i+57]
        P.append(a)
    except IndexError :
        pass

    P.sort()
    All.append(P[-1])

All.sort()
print(All[-1])
system("pause")














