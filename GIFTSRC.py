test_cases=int(input())
for i in range(test_cases):
    n=int(input())
    s=input()
    x,y=0,0
    for i in range(len(s)):
        if((i==0) or (s[i-1]!=s[i]) and ((s[i-1]=="L" and s[i]!="R") or (s[i-1]=="R" and s[i]!="L") or (s[i-1]=="U" and s[i]!="D") or (s[i-1]=="D" and s[i]!="U"))):
            print(s[i])
            if s[i]=="L":
                x-=1
            elif s[i]=="D":
                y-=1
            elif s[i]=="R":
                x+=1
            elif s[i]=="U":
                y+=1
    print(x,y)
