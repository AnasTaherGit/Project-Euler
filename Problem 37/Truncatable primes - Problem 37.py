def is_prime(n):

    if n <= 1:
        return False

    else:
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1

        return True


def is_truncable(n, d):
    if d == 'right':
        if len(str(n)) == 1:
            return is_prime(n)

        else:
            if is_prime(n):
                return is_truncable(n // 10, 'right')
            else:
                return False
    else:
        if len(str(n)) == 1:
            return is_prime(n)

        else:
            if is_prime(n):
                return is_truncable(n % 10**(len(str(n)) - 1), 'left')
            else:
                return False


S = 0
count = 0
n = 11
while count < 11:
    if is_prime(n):
        if is_truncable(n, 'right') and is_truncable(n, 'left'):
            S += n
            count += 1

    n += 1

print(S)
