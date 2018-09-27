def is_palindromeBase(n, b):

    M = []
    while n != 0:
        M.append(n % b)
        n = n // b

    for i in range(0, len(M) // 2 + 1):
        if M[i] != M[-i - 1]:
            return False

    return True


S = 0

for n in range(1, 10**6):
    if is_palindromeBase(n, 2) & is_palindromeBase(n, 10):
        S += n

print(S)
