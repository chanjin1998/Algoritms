import sys
n = int(sys.stdin.readline())

def dp(n):
  if n == 1:
    return 1
  if n ==2 :
    return 3
  arr = [0,1,3]
  for i in range(3,n+1):
    num = arr[i-1] + arr[i-2]*2
    arr.append(num)
  return arr[n]

print(dp(n)%10007)