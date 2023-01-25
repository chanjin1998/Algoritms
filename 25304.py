import sys
price = int(sys.stdin.readline())
N = int(sys.stdin.readline())
val = []
sum = 0
for i in range(N):
    val.append(sys.stdin.readline().split())
for j in range(N):
    sum += int(val[j][0])*int(val[j][1])
if sum == price:
    print("Yes")
else:
    print("No")