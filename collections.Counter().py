from collections import Counter
n=int(input())
shoe_size=list(map(int,input().split()))
person=int(input())
dic=Counter(shoe_size)
price=0
for i in range(person):
    size,pr=map(int,input().split())
    if dic[size]>0:
        price+=pr
        dic[size]-=1
print(price)
