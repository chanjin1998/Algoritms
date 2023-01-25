import sys
import math
from collections import Counter
N_list = []
N = int(sys.stdin.readline())
for i in range(N):
    N_list.append(int(sys.stdin.readline()))
N_list.sort()
print(round(sum(N_list)/N))
print(N_list[N//2])
f = Counter(N_list)
b = f.most_common()
if len(N_list) > 1:
    if b[0][1]==b[1][1]:
        print(b[1][0])
    else:
        print(b[0][0])
else:
    print(N_list[0])
print(N_list[-1]-N_list[0])
