import sys

n = int(sys.stdin.readline())
<<<<<<< HEAD
wine = [0]*10000
for i in range(n):
    wine[i] = (int(sys.stdin.readline()))
dp = [0]*10000
dp[0] = wine[0]
dp[1] = wine[0] + wine[1]
dp[2] = max(wine[0]+wine[2],wine[1]+wine[2],dp[1])
for i in range(3,n):
  dp[i] = max(dp[i-2]+wine[i],dp[i-3]+wine[i-1]+wine[i],dp[i-1])
print(max(dp))
=======
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
>>>>>>> parent of d283db6 (파일 정리)
