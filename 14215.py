import sys
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()
if arr[2] >= arr[0] + arr[1]:
  arr[2] = arr[0] + arr[1] -1
print(arr[0]+arr[1]+arr[2])