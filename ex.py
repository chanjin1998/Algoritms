import sys
n,c = map(int,sys.stdin.readline().split())
location = []
visited = []
for i in range(n):
  if i == 0 or i == (n-1):
    visited.append(1)
    location.append(int(sys.stdin.readline()))
  else:
    visited.append(0)
    location.append(int(sys.stdin.readline()))

location.sort()

cnt = 2
tmp[0].append(location[0])
tmp[n-1].append(location[n-1])
start = 0
end = n - 1
temp = 0
while (cnt<c):
  tmp = [[n] for _ in range(n)]

  for i in range(1,n-1):
    if visited[i] == 0:
      tmp[i].append(min(location[i] - location[start]),(location[end] - location[i]))
  
  tmp = sorted(tmp, key=lambda x: x[1])
  temp = tmp[-1][1]
  cnt += 1
print(temp)
  