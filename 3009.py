import sys
from collections import Counter
val = []
val1 = []
rec = []
answer = ''
for i in range(3):
    rec += list(map(int,sys.stdin.readline().split()))
val = [rec[0],rec[2],rec[4]]
val1 = [rec[1],rec[3],rec[5]]
for j in range(3):
    if val.count(val[j]) == 1:
        answer = str(val[j])+' '
for k in range(3):
    if val1.count(val1[k]) == 1:
        answer += str(val1[k])
print(answer)

