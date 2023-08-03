import sys
n, m = map(int,sys.stdin.readline().split())
im = 0
arr = [j for j in range(1,n+1)]
for i in range(m):
  a,b = map(int,sys.stdin.readline().split())
  im = arr[a-1]
  arr[a-1] = arr[b-1]
  arr[b-1] = im

for k in range(n):
  print(arr[k],end=' ')
