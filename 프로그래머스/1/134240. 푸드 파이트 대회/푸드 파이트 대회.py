def solution(food):
    answer = ''
    result = []
    for i in range(1,len(food)):
        tmp = str(i) * ((food[i]//2))
        if '0' in tmp:
            pass
        else:
            result.append(tmp)
            answer += tmp
    answer += '0'
    for i in range(len(result)-1,-1,-1):
        answer += result[i]
    return answer