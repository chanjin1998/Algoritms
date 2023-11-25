def solution(num_list):
    answer = []
    val = 0
    odd_val = 0
    for i in num_list:
        if i % 2 == 0:
            val += 1
        else:
            odd_val += 1
    return val,odd_val