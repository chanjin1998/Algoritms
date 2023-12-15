def solution(num_list):
    sum_answer = 0
    mul_answer = 1
    if len(num_list)>=11:
        for i in num_list:
            sum_answer+= i
        return sum_answer
    else:
        for i in num_list:
            mul_answer *= i
        return mul_answer