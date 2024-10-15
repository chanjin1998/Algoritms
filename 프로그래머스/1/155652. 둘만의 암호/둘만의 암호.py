def solution(s, skip, index):
    answer = ''
    skip_num = []
    for tmp in skip:
        skip_num.append(ord(tmp))
    for alpha in s:
        cnt = 0
        tmp = ord(alpha)
        while cnt < index:
            tmp += 1
            if tmp == 123:
                tmp = 97
            if tmp in skip_num:
                pass
            else:
                cnt +=1
        answer += chr(tmp)
    return answer
#97-122