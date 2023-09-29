import sys
n = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))
ans = []
max_d = -int(1e9)
max_diff = 0
visited = [0 for _ in range(n)]
def dfs():
  global max_d,max_diff
  if len(ans) == n:
    for i in range(n-1):
      max_diff += abs(ans[i] - ans[i+1])
    max_d = max(max_d,max_diff)
    max_diff = 0
    return
  for i in range(n):
    if visited[i] == 0:
      visited[i] = 1
      ans.append(num[i])
      dfs()
      visited[i] = 0
      ans.pop()
dfs()
print(max_d)