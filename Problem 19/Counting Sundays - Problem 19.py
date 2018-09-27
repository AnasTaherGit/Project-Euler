MOIS_1=[31,28,31,30,31,30,31,31,30,31,30,31]
MOIS_2=[31,29,31,30,31,30,31,31,30,31,30,31]
D=0
N=0
for M in MOIS_1:
    for J in range(1,M+1):
        D=(D+1)%7
print(D)        
for Y in range(1901,2001):
    #print(Y)
    if (Y%4==0 and Y%100!=0)or(Y%400==0):
        for M in MOIS_2:
            for J in range(1,M+1):
                if J==1 and D==6:
                    N=N+1
                D=(D+1)%7            
    else:
        for M in MOIS_1:
            #print(M)
            for J in range(1,M+1):
                #print(D,J)
                if J==1 and D==6:
                    #print(D,J)
                    N=N+1
                D=(D+1)%7

print(N)    

