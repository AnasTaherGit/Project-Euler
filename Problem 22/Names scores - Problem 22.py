with open('Annexe - Problem 22.txt') as f :
    c=f.read().split('","')

c.sort()
ALPHABET="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def f(m):
    N=[]
    for l in m:
        N.append(ALPHABET.index(l)+1)
    return sum(N)

def main():
    s=0
    for m in range(0,len(c)):
       s=s+f(c[m])*(m+1)
    print(s)

main()
input("Press enter to continue ...")

        
