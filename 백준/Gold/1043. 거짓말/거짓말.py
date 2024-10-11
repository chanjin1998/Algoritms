import sys
n,m = map(int,sys.stdin.readline().split())
know = set(sys.stdin.readline().split()[1:])
parties = []
cnt = 0
for _ in range(m):
  parties.append(set(sys.stdin.readline().split()[1:]))
for _ in range(m):
  for party in parties:
    if party & know:
      know = know.union(party)

for party in parties:
  if party & know:
    continue
  cnt += 1
print(cnt)