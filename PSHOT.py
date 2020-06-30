def check(n,s):
    a=0
    b=0
    for i in range(2,len(s)+1,2):
        a+=int(s[i-2])
        if(abs(a-b)>(n-((i-1)//2))):return(i-1)
        b+=int(s[i-1])
        if(abs(a-b)>(n-(i//2))):return(i)
    return(n*2)
for _ in range(int(input())):
    n=int(input())
    s=input()
    print(check(n,s))
