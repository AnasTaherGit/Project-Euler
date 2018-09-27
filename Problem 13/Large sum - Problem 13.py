from os import system

with open("Annexe - Problem 13.txt") as f:
    D=f.read().split()
def conv(x):
    k=int(x)
    return k
D=list(map(conv,D))

S=0

for element in D :
   S=S+element

S=str(S)
p=S[0:10]
print(int(p))

system("pause")
