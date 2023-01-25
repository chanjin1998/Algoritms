# import sys
# n,m = map(int,sys.stdin.readline().split())
# def gcd(n,m):
#     while(m):
#         n,m = m,n%m
#     return n
# def lcm(n,m):
#     result = (n*m)//gcd(n,m)
#     return result
# print(lcm(n,m))
import sys
T = int(sys.stdin.readline())
for i in range(T):
    n,m = map(int,sys.stdin.readline().split())
    def gcd(n,m):
        while(m):
            n,m = m,n%m
        return n
    def lcm(n,m):
        result = (n*m)//gcd(n,m)
        return result
    print(lcm(n,m))