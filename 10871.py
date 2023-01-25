import sys
a = []
N, X = map(int,sys.stdin.readline().split(' '))
# for i in range(N):
a = map(int,sys.stdin.readline().split(' '))
a = list(a)
for i in range(len(a)):
    if int(a[i])<X:
        print(a[i])
