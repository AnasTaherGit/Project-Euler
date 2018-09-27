def digits(n):

    M = []
    while n != 0:
        M.append(n % 10)
        n = n // 10
    # print(M)
    return M


def PGCD(a, b):

    if (abs(a) < abs(b)):
        a, b = b, a

    if b == 0:
        return a

    else:
        return PGCD(b, a % b)


fractions = []

for i in range(10, 100):
    for j in range(10, 100):
        if i != j and i / j < 1:
            a, b = digits(i), digits(j)

            if len(set(a)) == len(set(b)):
                c = list(set(a) & set(b))
                if len(c) == 1 and c[0] != 0:

                    a.remove(c[0])
                    b.remove(c[0])
                    if b[0] != 0 and a[0] / b[0] == i / j:
                        fractions.append((i, j))


D = fractions[0][1] * fractions[1][1] * fractions[2][1] * fractions[3][1]
N = fractions[0][0] * fractions[1][0] * fractions[2][0] * fractions[3][0]
print(D // PGCD(N, D))
