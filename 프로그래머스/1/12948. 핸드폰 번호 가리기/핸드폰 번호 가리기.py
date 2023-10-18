def solution(phone_number):
    answer = ''
    p_len = len(phone_number)
    answer = ','.join(phone_number)
    p_list = list(map(str,answer.split(',')))
    for i in range(p_len-4):
        p_list[i] = '*'
    num = ''.join(p_list)
    return num