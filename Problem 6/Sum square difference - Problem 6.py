from os import system
def calcul_diff(n):
    U=(n*(n+1)/2)**2
    V=n*(n+1)*(2*n+1)/6
    return int(U-V)

print(calcul_diff(100))
system("pause")
