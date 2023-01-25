import sys
cnt = 0
n = int(sys.stdin.readline())
alpha = list(map(int,sys.stdin.readline().split()))
for i in range(len(alpha)-1):
    if abs(alpha[i] - alpha[i+1])>2:
        break
    if abs(alpha[i]-alpha[i+1])<=2:
        cnt +=1
    if i == len(alpha)-2:
        cnt +=1
print(cnt)