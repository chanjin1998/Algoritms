import sys
from collections import Counter
M = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))
N = int(sys.stdin.readline())
res = list(map(int,sys.stdin.readline().split()))
num.sort()

count = Counter(num)

for i in range(len(res)):
    if res[i] in count:
        print(count[res[i]],end=' ')
    else:
        print(0,end=' ')