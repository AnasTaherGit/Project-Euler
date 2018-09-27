P=lambda n,m:n**m

R=set()

for a in range(2,101):
    for b in range(2,101):
        k=P(a,b)
        R.add(k)
print(len(R))
