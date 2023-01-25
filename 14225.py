# import sys
# S = []
# val = []
# N, M = map(int,sys.stdin.readline().split())
# for i in range(N) :
#     S.append(sys.stdin.readline().strip())
# for j in range(M):
#     val.append(sys.stdin.readline().strip())
# S.sort()
# cnt = 0

# for k in val:
#     start = 0
#     end = len(S)-1
#     mid = (start+end)//2
#     while start<=end:
#         if S[mid] == k:
#             cnt +=1
#             break
#         elif S[mid] < k:
#             start = mid + 1
#         else:
#             end = mid - 1
#     print(cnt)
import sys
N,M = map(int,sys.stdin.readline().split())
S = set()
for i in range(N):
    S.add(sys.stdin.readline())
ans = 0
for j in range(M):
    t = sys.stdin.readline()
    if t in S:
        ans +=1
print(ans)