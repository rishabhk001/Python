from sys import stdout
def check(low,high):
    if low<high:
        if (low%2==0 and high%2==0) or (low%2!=0 and high%2!=0):
            mid=(low+high)//2
        else:
            mid=(low+high+1)//2
        n=[]
        print(mid)
        stdout.flush()
        n.append(input())
        if n[0]=='E':
            return
        print(mid)
        stdout.flush()
        n.append(input())
        if n[1]=='E':
            return
        print(mid)
        stdout.flush()
        n.append(input())
        if n[2]=='E':
            return
        print(mid)
        stdout.flush()
        n.append(input())
        if n[3]=='E':
            return
        if (n[0]=='G' and n[2]=='G') :
            check(mid,high)
        elif (n[0]=='L' and n[1]=='L'):
            check(low,mid)
        elif (n[1]=='L' and n[3]=='L'):
            check(low,mid)
        elif (n[1]=='G' and n[3]=='G'):
            check(mid,high)
n=int(input())
check(1,n)
