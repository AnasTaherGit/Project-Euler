from os import system
from time import clock
def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
t=clock()
S=0
for i in range(2,2*10**6):
    if is_prime(i):
        S=S+i
        
    
print(S)
print(t)
system("pause")
