def solution(s):
    answer = ''
    if s[0] == '-':
        for i in range(1,len(s)):
            answer += s[i]
        answer = int(answer)*(-1)
    elif s[0] == '+':
        for i in range(1,len(s)):
            answer += s[i]
        answer = int(answer)
    else:
        for i in range(len(s)):
            answer += s[i]
        answer = int(answer)
    return answer