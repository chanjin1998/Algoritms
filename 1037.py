import sys
N = int(sys.stdin.readline())
val = list(map(int,sys.stdin.readline().split()))
if N == 1:
    print(val[0]*val[0])
if N >=2:
    val.sort()
    print(val[0]*val[N-1])