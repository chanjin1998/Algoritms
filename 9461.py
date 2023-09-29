import sys
n = int(sys.stdin.readline())

def dp(n):
  if n == 1:
    return 1
  if n ==2 :
    return 1
  if n == 3:
    return 1
  if n == 4:
    return 2
  if n ==5 :
    return 2
  arr = [0,1,1,1,2,2]
  for i in range(6,n+1):
    arr.append(arr[i-1]+arr[i-5])
  return arr[n]
for _ in range(n):
  a = int(sys.stdin.readline())
  print(dp(a))
