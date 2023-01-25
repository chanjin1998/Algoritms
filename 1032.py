import sys
N = int(sys.stdin.readline())
file = []
res = []
for i in range(N):
    file.append(sys.stdin.readline())
res.append(file[0] or file[1] or file[2])
print(file[0] or file[1])