import sys
n, m = map(int,sys.stdin.readline().split())
# arr = [[0 for a in range(n)]for b in range(m)]
arr = []
arr1 = []
for i in range(n):
  arr.append(list(map(int,sys.stdin.readline().split())))
for j in range(n):
  arr1.append(list(map(int,sys.stdin.readline().split())))

for i in range(n):
  for j in range(m):
    print(arr[i][j] + arr1[i][j],end=' ')
  print()