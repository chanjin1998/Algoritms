import sys
n = int(sys.stdin.readline())
N = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
M = list(map(int,sys.stdin.readline().split()))
N.sort()
def bina(l,N,start,end):
    if start>end:
        return 0
    m = (start+end)//2
    if l == N[m]:
        return 1
    elif l < N[m]:
        return bina(l,N,start,m-1)
    else:
        return bina(l,N,m+1,end)

for l in M:
    start = 0
    end = len(N)-1
    print(bina(l,N,start,end))