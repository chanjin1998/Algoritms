def solution(number):
    answer = 0
    result = []
    def dfs(start):
        nonlocal answer
        if len(result) == 3:
            if sum(result) == 0:
                answer += 1
                return
            else:
                return

        for i in range(start,len(number)):
            result.append(number[i])
            dfs(i+1)
            result.pop()
    dfs(0)
    return answer