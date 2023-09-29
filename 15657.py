<<<<<<< HEAD
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
temp = []

def dfs(start):
    if len(temp) == m:
        print(*temp)
        return
    for i in range(start, n):
            temp.append(nums[i])
            dfs(i)
            temp.pop()

dfs(0)
=======
import sys
n,k = map(int,sys.stdin.readline().split())
for i in range(n):
    
>>>>>>> parent of d283db6 (파일 정리)
