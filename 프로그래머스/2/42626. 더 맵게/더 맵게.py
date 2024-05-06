import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        if scoville[0] >= K:
            break
        if len(scoville) == 1:
            return -1
        s_first = heapq.heappop(scoville)
        s_second = heapq.heappop(scoville)
        s_new = s_first + s_second * 2
        heapq.heappush(scoville, s_new)
        answer += 1

    return answer