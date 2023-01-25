import sys

N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
val = sorted(list(set(arr)))

dic = {val[i] : i for i in range(len(val))}
for i in arr:
    print(dic[i], end = ' ')


