import sys
n,k = map(int,sys.stdin.readline().split())
val = 1
alpha = 1
beta = 0
for i in range(n,n-k,-1):
    val*=i
    beta+=1
    alpha *= beta
print((val//alpha)%10007)
