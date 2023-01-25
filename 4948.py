import sys
import math
val = []
def prime():
    for i in range(123456*2+1):
        count = 0
        if i > 1:
            for j in range(2,int(math.sqrt(i)+1)):
                if i % j == 0:
                    count += 1
                    break
            if count == 0:
                val.append(i)
prime()
while (1):
    N = int(input())
    if N == 0:
        break
    cnt = 0
    for i in val:
        if N<i<=2*N:
            cnt +=1
    print(cnt)
