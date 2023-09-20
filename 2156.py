import sys

n = int(sys.stdin.readline())
wine = [0]
for _ in range(n):
    wine.append(int(sys.stdin.readline()))
dp = []
dp.append(0)
dp.append(wine[1])
dp.append(wine[1]+wine[2])
for i in range(3,n+1):
  dp.append(max(dp[i-2]+wine[i],dp[i-3]+wine[i-1]+wine[i],dp[i-1]))
print(max(dp))
# 와인을 먹지않는 경우도 포함