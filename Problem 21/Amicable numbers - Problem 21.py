def d(n):
    div=[1]
    for i in range(2,n):
        if n%i==0:
            if div.count(i)==0:
                div.append(i)
                div.append(n//i)
    #print(div)
    return sum(div)
AN=[]
for k in range(1,10000):
    p=d(k)
    if k==d(p)and p!=k:
        if AN.count(k)==0:
            AN.append(k)
            AN.append(p)

print(sum(AN))
input("press enter to continue ...")

           
