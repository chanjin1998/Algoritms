import sys
a = sys.stdin.readline().strip().split(':')
n = int(a[0])
m = int(a[1])

def gcd(n,m):
    if n>=m:
        while m>0:
            n, m = m, n%m
        return n
    else:
        while n>0:
            m,n = n,m%n
        return m
print("%d:%d"%(n//gcd(n,m),(m//gcd(n,m))))