def solution(n):
    answer = 0
    result = []
    for i in range(n-1,0,-1):
        if n % i == 1:
            result.append(i)
    answer = min(result)
    return answer