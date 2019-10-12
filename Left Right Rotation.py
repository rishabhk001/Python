a=[1,2,3,4,5,6,7]
print("1.Left Rotation\n2.Right Rotation")
n=int(input())
if(n==1 or n==2):
    print("No of rotations")
    k=int(input())
else:
    print("Choose correct option")
if(n==1):
    for i in range(k):
        l=a[0]
        a.remove(a[0])
        a.append(l)
    print(a)
if(n==2):
    for i in range(len(a)-k):
        l=a[0]
        a.remove(a[0])
        a.append(l)
    print(a)
