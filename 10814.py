import sys
N = int(input())
arr = []
for i in range(N):
    [a,b] = sys.stdin.readline().split()
    a = int(a)
    arr.append([a,b])
arr.sort(key = lambda x : x[0])
for i in range(N):
    print(arr[i][0],arr[i][1])