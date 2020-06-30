import math
def fact(n):
    fact=1
    for i in range(2,n):
        fact=fact+i
    return fact
c=int(input())
d=dict()
for _ in range(c):
    x,y,s=map(int,input().split())
    if x==0 and y==0:
        continue
    hypo1=math.sqrt((x/s)**2+(y/s)**2)
    #print(hypo,hypo1)
    if hypo1 not in d:
        d[hypo1]=1
    else:
        d[hypo1]+=1
    #print(d)
total=0
for k,v in d.items():
    if v==1:
        continue
    else:
        total+=fact(v)
print(total)
