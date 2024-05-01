import sys

n, m = map(int, input().split())
nick = [sys.stdin.readline().split() for _ in range(n)]
nick.sort(key=lambda x: int(x[1]))  # 오름차순 정렬

chars = [int(sys.stdin.readline().strip()) for _ in range(m)]

for char in chars:
    right = len(nick)
    left = 0
    result = 0
    while left <= right:
        mid = (left+right)//2
        if int(nick[mid][1]) >= char:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    print(nick[result][0])
ㅁㅇㅁㅇ