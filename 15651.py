import sys
n,m = map(int,sys.stdin.readline().split())

ans = []
def backtracking():
  if len(ans) == m:
    print(*ans)
    return
  for i in range(1,n+1):
    ans.append(i)
    backtracking()
    ans.pop()
backtracking()
