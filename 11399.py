import sys
n = int(sys.stdin.readline())
time = list(map(int,sys.stdin.readline().split()))
time.sort()
sum = 0
for i in range(len(time)):
    sum += time[i]*(len(time)-i)
print(sum)