import sys
h_name = set()
s_name = set()
N,M = map(int,sys.stdin.readline().split())
for i in range(N):
    h_name.add(sys.stdin.readline().strip())
for j in range(M):
    s_name.add(sys.stdin.readline().strip())
result = sorted(list(h_name & s_name))
print(len(result))
for k in result:
    print(k)