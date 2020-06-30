def boardgame(arr,n):
  for i in range(1,n):
    arr[0][i]=(arr[0][i-1])//2+arr[0][i]
  for i in range(1,n):
    arr[i][0]=(arr[i-1][0])//2+arr[i][0]
  for i in range(1,n):
    for j in range(1,n):
      arr[i][j]=min(arr[i-1][j]//2+arr[i][j],arr[i][j-1]//2+arr[i][j])
  return arr[n-1][n-1]
n=int(input())
arr=[]
for i in range(n):
  arr.append(list(map(int,input().split())))
print(boardgame(arr,n))
