import sys
N = int(sys.stdin.readline())
arr = []
cnt = 0
arr = list(map(int,sys.stdin.readline().split()))
v = int(sys.stdin.readline())
for i in arr:
  if i == v:
    cnt += 1
  else:
    pass
print(cnt)
