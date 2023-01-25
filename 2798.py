import sys
import random
N, M = map(int,sys.stdin.readline().split())
alpha = list(map(int,sys.stdin.readline().split()))
val = []
for i in range(len(alpha)):
    for j in range(i+1,len(alpha)):
        for k in range(j+1,len(alpha)):
            if alpha[i]+alpha[j]+alpha[k] <= M:
                val.append(alpha[i]+alpha[j]+alpha[k])
            else:
                continue
b = list(set(val))
print(max(b))