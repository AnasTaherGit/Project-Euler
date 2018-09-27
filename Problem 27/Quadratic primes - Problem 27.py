def is_prime(n):
    i=2
    while i**2<=n:
        if n%i==0:  return False

        i+=1

    return True

P=lambda n,a,b:n**2+a*n+b

def biggest_range(a,b):
    k=0
    for n in range(0,b):
        if not is_prime(abs(P(n,a,b))):
            k=n
            break
    return k

def main():
    maxi=0
    p=0
    for b in range(-999,1000):
        if not is_prime(b):
            continue
        for a in range(-999,1000):
            s=biggest_range(a,b)
            if s>maxi:
                maxi=s
                p=a*b
                x=a
                q=b
        #print(b)
    print(p)
    print(x)
    print(q)
    print(maxi)
    

main()
            

            
            
        
        
