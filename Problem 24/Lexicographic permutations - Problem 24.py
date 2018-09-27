from math import factorial as fact

nbrs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


n = 10**6
print('-------------------------------------')
s = ''
for i in range(0, 10):
    k = fact(9 - i)
    c = n // k
    n = n % k
    # print(nbrs)
    if n == 0:
        x = nbrs[c - 1]
        #print('x =',x,'and c =',c)
        s += str(x)
        nbrs.remove(x)
    else:
        x = nbrs[c]
        #print('x =',x,'and c =',c)
        s += str(x)
        nbrs.remove(x)

print(int(s))
