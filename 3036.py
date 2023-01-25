import sys
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
def gcd(n,m):
        while(m):
            n,m = m,n%m
        return n
for i in range(1,n):
    val = gcd(a[0],a[i])
    print('%d/%d'%(a[0]//val,a[i]//val))