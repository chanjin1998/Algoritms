def solution(hp):
    answer = 0
    
    a = hp // 5
    tmp = hp % 5
    b = tmp // 3
    tmp = tmp % 3
    answer = a + b + tmp
    return answer