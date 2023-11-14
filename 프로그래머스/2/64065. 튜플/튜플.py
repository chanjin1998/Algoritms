def solution(s):
    answer = ''
    res = []
    dic = {}
    result = []
    s = s[1:-1]
    for i in s:
        if i == '}' or i =='{':
            if len(answer) != 0:
                res.append(int(answer))
                answer = ''
            else:
                pass
        elif i == ',':
            if len(answer) != 0:
                
                res.append(int(answer))
                answer = ''
            else:
                pass
        else:
            answer += i
    dic = {item : 0 for item in set(res)}
    for val in res:
        dic[val] += 1
    dic = sorted(dic.items(),key = lambda x:x[1], reverse = True)
    for i in dic:
        result.append(i[0])
    return result