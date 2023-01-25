import sys
n,m = map(int,sys.stdin.readline().split())
apple = []
k = int(sys.stdin.readline())
for _ in range(k):
    apple.append(int(sys.stdin.readline()))
mv = 0
end = m
start = 1

for i in range(k):
    if end>= apple[i] and start <= apple[i]:
        continue
    elif end < apple[i]:
        mv += apple[i] - end
        end = apple[i]
        start = apple[i] - (m-1)
    elif start > apple[i]:
        mv += start - apple[i]
        start = apple[i]
        end = apple[i] + (m-1)
print(mv)