from collections import deque
def solution(arr):
    answer = []
    q = [arr[0]]
    # q = deque((1))
    # q.append(1)
    for i in range(1,len(arr)):
        if arr[i] not in q or arr[i-1] != arr[i]:
            q.append(arr[i])
    return q