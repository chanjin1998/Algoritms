import sys
# f(n) = f(n-1) + f(n-2) + f(n-3)
N = int(sys.stdin.readline())

def dp(n):
  if n == 1:
    return 1
  if n == 2:
    return 2
  if n == 3:
    return 4
  dp_arr = [0,1,2,4]

  for i in range(4,n+1):
    dp_arr.append(dp_arr[i-1] + dp_arr[i-2] + dp_arr[i-3])
  return dp_arr[n]

for i in range(N):
  num = int(sys.stdin.readline())
  print(dp(num))

# for i in range(N):
#   num = int(sys.stdin.readline())
#   res.append(dp(num))
# res2 = "\n".join(map(str,res))
# print(res2)