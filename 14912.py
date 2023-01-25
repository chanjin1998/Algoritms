import sys
n,k = map(str,sys.stdin.readline().split())
a = [i for i in range(1,int(n)+1)]
cnt = 0
for j in str(a):
    if k in j:
        cnt += 1
print(cnt)