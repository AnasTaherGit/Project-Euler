def is_sum(n,l=5):
    if sum([int(k)**l for k in str(n)])==n :
        return True
    return False

def digit(m,l=5):
    s=0
    for n in range(10**(m-1),10**m):
        #print(n)
        if is_sum(n,l):
            s=s+n
    return s

Sum=0
for i in range(2,7):
    Sum=Sum+digit(i)
print(Sum)    
    

        

