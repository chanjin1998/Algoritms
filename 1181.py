import sys
n = int(input())
arr = []
for i in range(n):
    arr.append(sys.stdin.readline().strip('\n'))
arr = list(set(arr))
arr.sort()
arr.sort(key=len)
for i in range(len(arr)):
    print(arr[i])