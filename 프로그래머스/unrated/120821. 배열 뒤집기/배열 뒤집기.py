def solution(num_list):
    answer = []
    res = []
    for i in range(len(num_list)-1,-1,-1):
        res.append(num_list[i])
    return res