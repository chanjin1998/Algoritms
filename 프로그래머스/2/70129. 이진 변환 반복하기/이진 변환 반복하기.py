def solution(s):
    answer = []
    zero_list = []
    cnt = 0
    while True:
        res = []
        for i in s:
            if i == '0':
                zero_list.append(i)
            else:
                res.append(i)
        s = str(bin(len(res))[2:])
        cnt += 1
        if s == '1':
            break
    
    return cnt, len(zero_list)