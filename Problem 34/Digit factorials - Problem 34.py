from math import factorial as fact


def digits(n):

    M = []
    while n != 0:
        M.append(n % 10)
        n = n // 10
    # print(M)
    return M


def is_curious(n):

    M = digits(n)

    if sum(list(map(fact, M))) == n:
        return True

    else:
        False


S = 0

for n in range(3, 10**5):
    if is_curious(n):
        S += n

print(S)
