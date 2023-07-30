# import sys
# n,k = map(int,sys.stdin.readline().split())
# circle = [i for i in range(1,n+1)]
# res = []
# cnt = k
# while (1):
#     if len(circle) == 0:
#         break
#     elif len(circle) == 2:
#         res.append(circle[0])
#         res.append(circle[1])
#         circle.remove(circle[0])
#         circle.remove(circle[0])
#     elif cnt > len(circle):
#         cnt = cnt%len(circle)
#         res.append(circle[cnt-1])
#         circle.remove(circle[cnt-1])
#         cnt += 2
#     else :
#         res.append(circle[cnt-1])
#         circle.remove(circle[cnt-1])
#         cnt += 2
# print('<',end='')
# for i in range(len(res)):
#     if i == len(res)-1:
#         print(res[i],end='')
#     else:
#         print(res[i],end=', ')
# print('>')
import sys

n, k = map(int, sys.stdin.readline().split())

idx = 0
queue = [i for i in range(1, n+1)]
res = []
while queue:
    idx += k - 1
    if idx >= len(queue):
        idx %= len(queue)
    res.append(str(queue.pop(idx)))

print("<", ", ".join(res), ">", sep="")
