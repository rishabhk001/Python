import math
n1,n2=map(int,input().split())
arr1=[]
for i in range(n1,n2+1):
    c=0
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            c=1
            break
    if c==0:
        arr1.append(i)
s=""
arr2=[]
i=0
j=0
while(j<len(arr1)):
    if i!=j:
        s=str(arr1[j])+str(arr1[i])
        c=0
        for k in range(2,int(math.sqrt(int(s)))+1):
            if int(s)%k==0:
                c=1
                break
        if c==0 and int(s) not in arr2:
            arr2.append(int(s))
    i+=1
    if i==len(arr1):
        j+=1
        i=0
arr2.sort()
n=len(arr2)
i=arr2[0]
j=arr2[n-1]
print(arr2,i,j)
c=2
if n==1:
    print(i)
elif n==2:
    print(j)
else:
    while(c<n):
        k=i+j
        i=j
        j=k
        c+=1
    print(j)
