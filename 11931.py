import sys
n = int(sys.stdin.readline())
num = [0 for x in range(n)]
for i in range(n):
    num[i] = int(sys.stdin.readline())
num.sort(reverse = True)
for j in range(n):
    print(num[j])