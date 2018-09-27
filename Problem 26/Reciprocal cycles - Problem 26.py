def cycle_len(d):
    if d==1 : return -1
    i=2
    while 10**i%d!=1:
        i=i+1
        #print('h=',i)
    return i

def main():
    maxi=-1
    n=None
    #print('x')
    for i in range(2,1000):
        #print(i)
        d=i
        #print('x1')
        if d%2==0 or d%5==0:
            #print('x2')
            while d%2==0:
                d=d//2
                #print('x3')
            while d%5==0:
                d=d//5
                #print('x4')
        c=cycle_len(d)
        #print('x5')
        if c>maxi:
            maxi=c
            n=i
        
    print(n)

main()
