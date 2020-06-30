test=int(input())
for _ in range(test):
    n,b,m=map(int,input().split())
    arr=list(map(int,input().split()))
    c=0
    index=-1
    first=0
    for i in arr:
        if i//b!=index:
            c+=1
            index=i//b
    print(c)
            
