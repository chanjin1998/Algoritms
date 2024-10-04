import heapq
def solution(x, y, n):
    answer = 0
    INF = int(1e6)
    dp = [INF for _ in range(INF + 1)]
    def di(start):
        q = []
        heapq.heappush(q,(start,0))
        while q:
            now, cnt = heapq.heappop(q)
            if dp[now] < cnt:
                continue
            if now * 2 < INF+1:
                if cnt + 1 < dp[now*2]:
                    dp[now*2] = cnt + 1
                    heapq.heappush(q,(now*2,cnt+1))
            if now * 3 < INF+1:
                if cnt + 1 < dp[now*3]:
                    dp[now*3] = cnt + 1
                    heapq.heappush(q,(now*3,cnt+1))
            if now + n < INF+1:
                if cnt + 1 < dp[now+n]:
                    dp[now+n] = cnt + 1
                    heapq.heappush(q,(now+n,cnt+1))
    di(x)
    if x == y:
        return 0
    if dp[y] == INF:
        return -1
    else:
        return dp[y]

# x + n
# x * 2
# x * 3