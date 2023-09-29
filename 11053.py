import sys
n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))

dp_arr = [1] * n
for i in range(1,n):
  for j in range(i):
    if li[i] > li[j]:
      dp_arr[i] = max(dp_arr[i],dp_arr[j]+1)
print(max(dp_arr))