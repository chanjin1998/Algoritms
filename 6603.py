import sys

def dfs(start):
  if len(ans) == 6:
    print(*ans)
    return
  for i in range(start,n):
    ans.append(num[i])
    dfs(i+1)
    ans.pop()
while (True):
  num = list(map(int,sys.stdin.readline().split()))
  n = num[0]
  num.remove(num[0])
  ans = []
  dfs(0)
  print()
  if n == 0:
    break
