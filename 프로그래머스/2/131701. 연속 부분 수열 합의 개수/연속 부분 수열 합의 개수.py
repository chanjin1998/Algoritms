def solution(elements):
    answer = 0
    element = elements*2
    res = []
    sum_li = []
    def dfs(end):
        for i in range(len(elements)): # 0~4
            alpha = sum(element[i:i+end])
            res.append(alpha)

    for k in range(1,len(elements)+1): # 1~5
        dfs(k)
    return len(set(res))
