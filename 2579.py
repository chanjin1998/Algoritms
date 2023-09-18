import sys
n = int(sys.stdin.readline())
cost = [0]
for _ in range(n):
  cost.append(int(sys.stdin.readline()))

def dp(n):
  if n ==1 :
    return 10
  if n ==2 :
    return 30
  # if n == 3:
  #   return 35
  dp_arr = [0,10,30]

  for i in range(3,n+1):
    score = max(dp_arr[i-2],dp_arr[i-3]+cost[i-1]) + cost[i]
    dp_arr.append(score)
  return dp_arr[n]
print(dp(n))