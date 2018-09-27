from os import system

with open("Liste nombres premiers.txt") as f:
    D=f.read().split()
def conv(x):
    k=int(x)
    return k
D=list(map(conv,D))

def Sum(n):
    return int(n*(n+1)/2)

def NbDiv(n):
    Div=[]
    N=1
    for element in D :
        if element<=n:
            a=0
            while n%element==0:
                n=n/element
                a+=1
            Div.append(a)
        else:
            break
    for element in Div:
       N=N*(1+element)
        
    return N

    
def is_triangle(n):
    if NbDiv(n)>=500:
        return True
    else:
        return False

n=1
while not is_triangle(Sum(n)):
    n+=1

system("pause")
print(Sum(n))
