import sys
n,m = map(int,sys.stdin.readline().split())
arr = []
for i in range(1,n+1):
  if n % i == 0:
    arr.append(i)
try:
  print(arr[m-1])
except:
  print(0)