from os import system

S=0
p=2**1000
q=str(p)

for i in range(0,len(q)):
    S=S+int(q[i])

print(S)

system("pause")
