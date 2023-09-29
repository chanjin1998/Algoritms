import sys
n , s = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))
cnt = 0
ans = []
def dfs(start):
  global cnt
  if sum(ans) == s and len(ans)>0:
    cnt += 1
    # return
    # 왜 리턴을 안 받지....
  
  for i in range(start,n):
    ans.append(nums[i])
    dfs(i+1)
    ans.pop()
dfs(0)
print(cnt)

# ans = 0-5 0, 1-5 1 2-5 2 3-5 3 4-5 4
# 01234
# 0124
# 0134
# 014
# 0234
# 024
# 034
# 04
# 1234
# 124
# 134
# 14
# 234
# 24
# 34
# 4