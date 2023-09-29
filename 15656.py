import sys
n,m = map(int,sys.stdin.readline().split())
num = sorted(list(map(int,sys.stdin.readline().split())))

ans  = []
def back():
  if len(ans) == m:
    print(*ans)
    return
  for i in range(4):
    ans.append(num[i])
    
    back()
    ans.pop()
back()