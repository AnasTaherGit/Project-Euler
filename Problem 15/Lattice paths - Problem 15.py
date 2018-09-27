from os import system

def fact(n):
    if n==1 : return 1 
    else :return n*fact(n-1)

def C(n,p):
    return int(fact(n)/(fact(p)*fact(n-p)))

print(C(40,20))

system("pause")
