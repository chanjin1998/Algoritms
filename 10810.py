import sys
n,m = map(int,sys.stdin.readline().split())
arr = [0 for _ in range(n)]
for a in range(m):
  i,j,k = map(int,sys.stdin.readline().split())
  for b in range(i,j+1):
    arr[b-1] = k
for c in arr:
  print(c,end=' ')