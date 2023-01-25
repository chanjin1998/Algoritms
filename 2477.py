# import sys
# N = int(sys.stdin.readline())
# dir = []
# val = []
# for i in range(6):
#     a,b = map(int,sys.stdin.readline().split())
#     dir.append(a)
#     val.append(b)
# c = val.index(max(val))

# d = val.index(max(val[c-1],val[(c+1)%6]))   
# e = val.index(min(val[c-1],val[(c+1)%6]))

# if (e + 1)%6 == c:
#     print((val[c]*val[d]-((val[d]-val[e])*val[e-1]))*N)
# elif e - 1 == c:
#     print((val[c]*val[d]-((val[d]-val[e])*val[e+1]))*N)
import sys
input = sys.stdin.readline

n = int(input())
nList = []
w = h = w2 = h2 = 0
for i in range(6):
    dir, l = map(int, input().split())
    nList.append(l)
    # 가로와 세로의 최대값을 정해줌 (큰 사각형)
    if i % 2 == 0:
        w = max(w, l)
    else:
        h = max(h, l)

for i in range(6):
    if i % 2 == 0 and h == nList[(i+5) % 6]+nList[(i+1) % 6]:
        w2 = nList[i]
    elif i % 2 == 1 and w == nList[(i+5) % 6]+nList[(i+1) % 6]:
        h2 = nList[i]
print(n*(w*h - w2*h2))