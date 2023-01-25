# import sys
# n,k = map(int,sys.stdin.readline().split())
# val = [0 for x in range(n)]
# for i in range(n):
#     val[i] = list(map(int,sys.stdin.readline().split()))
# val.sort(key=lambda x : (int(x[1]),int(x[2]),int(x[3])),reverse = True)
# idx = 0
# rank = 0
# for i in range(n):
#     if val[i][0] == k:
#         idx = i
# if idx > 1:    
#     for j in range(idx):
#         if val[j][1]==val[idx][1]:
#             if val[j][2] == val[idx][2]:
#                 if val[j][3]==val[idx][3]:
#                     ans = idx - 1
#                 else:
#                     ans = idx
#             else:
#                 ans = idx
#         else:
#             ans = idx
# else:
#     ans = idx
# print(val)
# print(ans+1)         
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
s = []
for i in range(n):
    s.append(list(map(int, input().split())))
s.sort(key=lambda x : (-x[1], -x[2], -x[3]))
for i in range(n):
    if s[i][0] == k:
        index = i
for i in range(n):
    if s[index][1:] == s[i][1:]:
        print(i + 1)
        break