def solution(s):
    answer = ''
    num = len(s) // 2
    if len(s)%2 == 0:
        answer = s[num-1] + s[num]
    else:
        answer += s[num]
    return answer