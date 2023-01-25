import sys
T = int(input())

for i in range(T):
    n,l,v = 1,1,1
    a, b = map(int,sys.stdin.readline().split())
    for i in range(b,1,-1):
        n *=i
    for j in range(a,1,-1):
        l *=j
    for k in range(b-a,1,-1):
        v*=k
    print(n//(l*v))