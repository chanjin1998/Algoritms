import sys
N = int(input())

spe_num = list(map(int,sys.stdin.readline().split()))
real_cnt = 0
for i in range(N):
    count = 0
    if spe_num[i] == 1:
        continue
    elif spe_num[i] == 2:
        real_cnt +=1
        continue
    for j in range(2,int(spe_num[i]/2)+1):
        if spe_num[i] % j == 0:
            count += 1
            
    if count == 0:
        real_cnt +=1
print(real_cnt)
