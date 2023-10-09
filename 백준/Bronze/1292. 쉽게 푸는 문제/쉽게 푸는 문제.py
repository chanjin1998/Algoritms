import sys
a,b = map(int,sys.stdin.readline().split())
sum = 0
dp = []
for i in range(1,47):
  for j in range(i):
    dp.append(i)
for i in range(a-1,b):
  sum += dp[i]
print(sum)