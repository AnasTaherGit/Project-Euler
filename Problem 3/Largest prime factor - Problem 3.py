
""" The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ? """


import os
import pickle
from time import time

a=time()
fichier=open("Liste nombres premiers.txt","r")
contenu=fichier.read()
D=contenu.split()
fichier.close()
for i in range(0,len(D)):
    D[i]=int(D[i])


decomp_premier={}
n=600851475143
b=0
for e in D:
    while n%e==0:           
            n=n/e
            b+=1
            decomp_premier[e]=b
    b-=b

try:
    if len(decomp_premier)==1 and decomp_premier[e]==1:          
        print('le nombre que vous avez saisi est "premier".')
          
    else:     
        for cle,valeur in decomp_premier.items():
            print(cle ,"à la puissance",valeur)
              
except:
        for cle,valeur in decomp_premier.items():
            print(cle ,"à la puissance",valeur)
b=time()
print(b-a)
os.system("pause")
