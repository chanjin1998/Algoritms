import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

sorted_arr = sorted(arr)
res = []
for i in range(n):
  idx = sorted_arr.index(arr[i])
  res.append(idx)
  sorted_arr[idx] = -1
print(*res)