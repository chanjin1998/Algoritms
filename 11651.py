import sys
n = int(sys.stdin.readline())
array = []
for i in range(n):
    [a,b] = map(int,input().split())
    array.append([b,a])
s_arry = sorted(array)
for i in range(n):
    print(s_arry[i][1],s_arry[i][0])