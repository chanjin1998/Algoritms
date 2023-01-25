import sys
n = int(sys.stdin.readline())
birth = [0 for x in range(n)]
for i in range(n):
    birth[i] = list(sys.stdin.readline().split())
birth.sort(key=lambda x : (int(x[3]),int(x[2]),int(x[1])))
print(birth)
print(birth[-1][0])
print(birth[0][0])