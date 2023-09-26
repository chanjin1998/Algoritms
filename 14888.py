import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
a, b, c, d = map(int, sys.stdin.readline().split())
max_ans = -sys.maxsize - 1
min_ans = sys.maxsize


def backtracking(num, idx, add, sub, mul, div):
    global max_ans, min_ans
    if idx == n:
        max_ans = max(max_ans, num)
        min_ans = min(min_ans, num)
        return
    if add > 0:
        backtracking(num + nums[idx], idx + 1, add - 1, sub, mul, div)
    if sub > 0:
        backtracking(num - nums[idx], idx + 1, add, sub - 1, mul, div)
    if mul > 0:
        backtracking(num * nums[idx], idx + 1, add, sub, mul - 1, div)
    if div > 0:
        backtracking(int(num / nums[idx]), idx + 1, add, sub, mul, div - 1)

backtracking(nums[0], 1, a, b, c, d)
print(max_ans, min_ans)