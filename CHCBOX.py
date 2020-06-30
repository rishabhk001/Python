test_cases=int(input())
for j in range(test_cases):
    n=int(input())
    arr=list(map(int,input().split()))
    m=len(arr)//2
    max1=max(arr)
    count=0
    for i in range(n):
        if i+m<=n:
            if max1 not in arr[int(i):int(i+m)]:
                count+=1
        else:
            diff=int((i+m)-n)
            if max1 not in arr[i:n] and max1 not in arr[0:diff]:
                count+=1
    print(count)
