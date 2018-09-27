from time import time


def digits(n):

    M = []
    while n != 0:
        M.append(n % 10)
        n = n // 10
    # print(M)
    return M


def is_pandangital(n, d):

    P = digits(n) + digits(d[0]) + digits(d[1])

    for i in range(1, 10):

        if P.count(i) != 1:

            return False

    return True


def div(n):

    d = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            d.append((i, n // i))
        i += 1
    return d


a = time()
Panda = []

for n in range(0, 10000):

    for d in div(n):
        if is_pandangital(n, d):

            Panda.append(n)
            break
    # print(n)

print(sum(Panda))
print(time() - a)
