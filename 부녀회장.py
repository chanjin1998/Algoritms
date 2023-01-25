# 3행 : 1 4 9 16 31 52
# 2행 : 1 3 6 10 15 21
# 1행 : 1 2 3 4  5  6

import sys

a,  b = map(int,sys.stdin.readline().split())
apart = [[1 for col in range(1)]for row in range(a)]
print(apart)
cnt = 0
for i in range(0,a):
    for j in range(0,b-1):
        cnt +=1
        apart[i][j] = cnt
print(apart)
# for i in range(0,a):
#     apart[i][0] = 1
# for k in range(1,a):
#     for l in range(1,b):
#         apart[k][l] = apart[k-1][l] + apart[k][l-1]
# print(apart[a-1][b-1])