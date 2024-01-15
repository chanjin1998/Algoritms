import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
S = sys.stdin.readline().strip()

cnt = 0
word = ''

for i in range(N):
  word += 'IO'
word += 'I'

for i in range(M):
  if word in S[i:i+len(word)]:
    cnt += 1
print(cnt)