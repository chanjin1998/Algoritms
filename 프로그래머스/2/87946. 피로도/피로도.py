def solution(k, dungeons):
    tmp = k
    result = []
    value = []
    def dfs():
        nonlocal tmp
        if len(result) == len(dungeons):
            answer = 0
            a = tmp
            for idx in result:
                if a >= dungeons[idx][0]:
                    a -= dungeons[idx][1]
                    answer += 1
            value.append(answer)
            return
        
        for i in range(len(dungeons)):
            if i not in result:
                result.append(i)
                dfs()
                result.pop()
    dfs()
    return max(value)