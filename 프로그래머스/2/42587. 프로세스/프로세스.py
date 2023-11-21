def solution(priorities, location):
    answer = 0
    idx = 0
    length = len(priorities)
    while priorities[location] != 0:
        if priorities[idx%length] == max(priorities):
            priorities[idx%length] = 0
            answer += 1
        idx += 1
    return answer