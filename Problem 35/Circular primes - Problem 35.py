def is_prime(n):

    i = 2
    while i * i <= n:
        if n % i == 0:

            return False
        i += 1

    return True


def permutation(n):

    m = len(str(n))
    s = n % 10
    n = n // 10
    n = n + s * 10**(m - 1)

    return n


def permuted_prime(n):

    m = permutation(n)
    while (m != n):
        if not is_prime(m):
            return False
        m = permutation(m)

    return True


N = 13
for n in range(101, 10**6, 2):
    if is_prime(n):
        if permuted_prime(n):

            N += 1

print(N)
