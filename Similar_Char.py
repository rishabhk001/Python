string_len=int(input())
string=input()
l=[0]*string_len
d={i:0 for i in string}
print(d)
for i in range(string_len):
    l[i]=d[string[i]]
    d[string[i]]+=1
print(d)
print(l)
q=int(input())
for i in range(q):
    index=int(input())
    print(l[index-1])
