import time
a=time.time()
with open("Annexe - Problem 18.txt") as f:
    c=f.read().split()


for i in range (0,len(c)):
    c[i]=int(c[i])

triangle=[]
row=15
k=0
j=1
for i in range(1,row+1):
    triangle.append(c[k:j])
    k+=i
    j+=i+1

for x in range(0,row):
    for y in range(0,row-x):
        try:
            if triangle[row-x-1][y]>triangle[row-x-1][y+1]:
                triangle[row-x-2][y]+=triangle[row-x-1][y]
            else:
                triangle[row-x-2][y]+=triangle[row-x-1][y+1]
        except IndexError:
            pass

print(triangle[0][0])

b=time.time()
print(b-a)

