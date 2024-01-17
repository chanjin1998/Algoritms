def solution(citations):
    answer = []
    res = []
    citations.sort()
    for i in range(0,max(citations)+1):
        up_cnt = 0
        down_cnt = 0
        for val in citations:
            if val >= i:
                up_cnt += 1
            elif val<=i:
                down_cnt += 1
        if up_cnt>= i and down_cnt<=i:
            res.append(i)
    return max(res)

# 0 1 3 5 6 나머지 논문이 h번 이하 -> h의 최대가 h0-index
# 0번 이상 5개
# 1번 이상 4개 그러나  1번이상 4개 1번 이하 2개
# 2번 이상 3개 2개
# 3번 이상 3개 
# 4번 이상 2개  4번 이상 2개 너미즈 