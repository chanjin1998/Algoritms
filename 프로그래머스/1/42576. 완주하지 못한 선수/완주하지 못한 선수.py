def solution(participant, completion):
    d = dict()
    res = []
    for i in participant:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in completion:
        if i in d:
            d[i] -= 1
    for i in d.keys():
        if d[i]>= 1:
            res.append(i)
    
    return "".join(res)