def solution(answers):
    answer = []
    first = [1,2,3,4,5]
    f = len(first)
    f_res = 0
    second = [2,1,2,3,2,4,2,5]
    s = len(second)
    s_res = 0
    third = [3,3,1,1,2,2,4,4,5,5]
    t = len(third)
    t_res = 0
    for i in range(1,len(answers)+1):
        if first[i%f-1] == answers[i-1]:
            f_res += 1
        if second[i%s-1] == answers[i-1]:
            s_res += 1
        if third[i%t-1] == answers[i-1]:
            t_res += 1
    best = max(f_res,s_res,t_res)
    if f_res == best:
        answer.append(1)
    if s_res == best:
        answer.append(2)
    if t_res == best:
        answer.append(3)
    return answer