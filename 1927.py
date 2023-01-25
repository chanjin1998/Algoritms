import sys

N = int(sys.stdin.readline())
val = []
res = []
for i in range(N):
    x = int(sys.stdin.readline())
    if len(val) == 0 and x == 0:
        res.append(0)
    elif x == 0:
        res.append(val[0])
        val.remove(val[0])
    else:
        val.append(x)
        val.sort()
for j in range(len(res)):
    print(res[j])