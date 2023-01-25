import sys
import math

M, N = map(int,sys.stdin.readline().split())
for i in range(M,N+1):
    count = 0
    if i > 1:
        for j in range(2,int(math.sqrt(i)+1)):
            if i % j == 0:
                count +=1 
                break
        if count ==0:
            print(i)
