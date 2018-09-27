


''' By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number? '''


import os
import os
import pickle
fichier=open("Liste nombres premiers.txt","r")
contenu=fichier.read()
prime=contenu.split()
fichier.close()
for i in range(0,len(prime)):
    prime[i]=int(prime[i])

print(prime[10000])

os.system("pause")
