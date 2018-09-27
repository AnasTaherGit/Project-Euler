""" Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms. """


import os
FibEven=[2]
fib0=1
fib=2
while fib<4*(10**6):
    q=fib
    fib=fib+fib0
    fib0=q
    if fib%2==0:
        FibEven.append(fib)
Sum=0
for i in range(0,len(FibEven)):
    Sum=Sum+FibEven[i]

print(Sum)

os.system("pause")