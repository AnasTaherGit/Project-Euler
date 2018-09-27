from os import system

a=232000000
b=252000000
for i in range (a,b+1):
    c=0
    for j in range(1,21):        
        if i%j==0:
            c+=1
    if c==20:
        print(i)
        break

            
print('finish')

system("pause")
