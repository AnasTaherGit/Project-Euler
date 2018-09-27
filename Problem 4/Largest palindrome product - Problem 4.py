from os import system
def is_palind(n):
    n=str(n)
    l=int(len(n)/2)
    a=n[0:l]
    b=n[l:]
    b=b[::-1]
    if a==b:
        return True

palindrome=[]

for i in range(100,1000):
    for j in range(100,1000):
        if is_palind(i*j)==True:
            palindrome.append(i*j)
palindrome.sort()
print(palindrome[-1])

system("pause")

