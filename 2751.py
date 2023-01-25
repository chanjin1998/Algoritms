import sys
val = []
N = int(sys.stdin.readline())
for i in range(N):
    val.append(int(sys.stdin.readline().strip()))
val.sort()
for j in range(N):
    print(val[j])