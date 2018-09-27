from math import sqrt
import os
pyth_liste=[]
for x in range(1,1000):
    for y in range(1,1000):
        b=sqrt((x**2)+(y**2))
        z=int(b)
        if (z-b)==0:
             pyth_liste.append((x,y,z))

            
for i in range(0,len(pyth_liste)):
    a=pyth_liste[i]
    if a[0]+a[1]+a[2]==1000:
        print(a[0]*a[1]*a[2])
        break
    
os.system("pause") 
