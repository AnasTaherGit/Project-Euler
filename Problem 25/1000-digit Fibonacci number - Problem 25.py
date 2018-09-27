from math import sqrt


def fib(n):
    if n==1:return 1 
    if n==2:return 1 
    else: return lib[-1]+lib[-2]
lib=[1,1]
i=1
k=fib(i)
p=len(str(k))
while (p<1000):
    #print(p) 
    i+=1
    k=fib(i)
    p=len(str(k))
    lib.append(k)
    del lib[0]

print(i)


    
