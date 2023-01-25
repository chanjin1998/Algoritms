import sys
n,k = map(int,sys.stdin.readline().split())
fruit = list(map(int,sys.stdin.readline().split()))
fruit.sort()
for i in fruit:
    if k>=i:
        k+=1
    else:
        break
print(k)