def d(n):
    S=1
    p=2
    while p**2<=n:
        if n%p==0:
            #print(p,n//p)
            S+=p
            if (p!=n//p):S+=(n//p)
        p+=1
    return S



Abundant=[]
for i in range(2,28124):
    if d(i)>i:
        Abundant.append(i)
#print(len(Abundant))
def is_sum_abundant(n):
    for i in Abundant:
        k=n-i
        if (d(k)>k) and k>0:
            #print(i,k)
            return True
    return False
#print(is_sum_abundant(12))

S=0
for n in range(24,28124):
    #print(n)
    if is_sum_abundant(n):
        S+=n
    
N=28123*28124//2
print(N-S)
     
