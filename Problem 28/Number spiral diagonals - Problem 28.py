def spiral(n):
    if n==1: return 1
    else : return 4*n**2-6*n+6+spiral(n-2)

print(spiral(1001))
