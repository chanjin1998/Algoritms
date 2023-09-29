import sys
n,m = map(int,sys.stdin.readline().split())
num_li = sorted(list(map(int,sys.stdin.readline().split())))
ans = []
res = []
def back(start):
  if len(ans) == m:
    print(*ans)
    return
  remember = 0
  for i in range(start,n):
    if remember != num_li[i]:
      ans.append(num_li[i])
      remember = num_li[i]
      back(i)
      ans.pop()

back(0)