import sys
import math
N = int(sys.stdin.readline())
res = []
res1 = []
alpha = ''
for i in range(2,1000):
    cnt = 0
    for j in range(2,int(math.sqrt(i))+1):
        if i % j == 0:
            cnt +=1
    if cnt == 0:
        res.append(i)
for k in range(len(res)-1):
    res1.append(res[k]*res[k+1])
for l in res1:
    if l > N:
        alpha = l
        break
print(alpha)