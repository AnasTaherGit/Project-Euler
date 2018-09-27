from os import system

def Collatz(n):
    seq=[]
    seq.append(n)
    while n!=1:
        if n%2==0:
            n=int(n/2)
            seq.append(n)
        else :
            n=3*n+1
            seq.append(n)
    return seq

p,k=0,0    
for i in range(1,10**6):
    if len(Collatz(i))>p:
        p,k=len(Collatz(i)),i

print(k)

system("pause")
