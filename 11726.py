import sys
n = int(sys.stdin.readline())
# f(n) = f(n-1) + f(n-2)

def dp(n):
  if n == 1:
    return 1
  if n == 2:
    return 2
  dp_arr = [0,1,2]

  for i in range(3,n+1):
    dp_arr.append(dp_arr[i-1]+dp_arr[i-2])
  return dp_arr[n] % 10007

print(dp(n))
