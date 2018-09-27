def fact(n):
    if n=0:
        return 1
    else :
        return n*fact(n-1)

q=str(fact(100))
l=[q[i] for i in range(0,len(q))]
S=sum(list(map(int,l)))
print(S)


