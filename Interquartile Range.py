n=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l=[]
for i in range(n):
    for j in range(l2[i]):
        l.append(l1[i])
l=sorted(l)
m=l[0:len(l)//2]
if len(l)%2==0:
    n=l[len(l)//2:len(l)]
else:
    n=l[len(l)//2+1:len(l)]
if len(m)%2==0:
    q1=((m[(len(m)//2)-1])+(m[((len(m)//2))]))/2
    q2=(n[((len(n)//2)-1)]+(n[((len(n)//2))]))/2
else:
    q1=m[(len(m)//2)]
    q2=n[(len(n)//2)]
print(float(q2-q1))
