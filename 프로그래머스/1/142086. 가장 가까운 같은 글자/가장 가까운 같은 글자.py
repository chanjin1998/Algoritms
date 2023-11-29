def solution(s):
    result = [-1]
    for i in range(1,len(s)):
        answer = 0
        for j in range(i):
            if s[i] == s[j]:
                answer = i - j
            else:
                pass
        if answer == 0:
            result.append(-1)
        else:
            result.append(answer)
    return result