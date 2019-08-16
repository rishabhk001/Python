import math
n=int(input())
l=list(map(int,input().split()))
mean=sum(l)/n
sd=0
for i in range(n):
    sd+=pow((l[i]-mean),2)
print(round(math.sqrt(sd/n),1))
