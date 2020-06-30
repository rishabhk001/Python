n=int(input())
v5=(n-4)//5
if((n-v5*5)%2==0):
    v1=2
else:
    v1=1
v2=(n-v5*5-v1*1)//2
print(v1+v2+v5,v1,v2,v5)
