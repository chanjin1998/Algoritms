import math

M = int(input())
N = int(input())
num_list = []
for i in range(M,N+1):
    count = 0
    if i > 1:
        for j in range(2,int(math.sqrt(i))+1):
            if i % j == 0:
                count +=1
                break

        if count == 0:
            num_list.append(i)
if len(num_list)>0:
    print(sum(num_list))
    print(min(num_list))
else:
    print(-1)