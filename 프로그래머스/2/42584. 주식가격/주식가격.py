def solution(prices):
    answer = []
    for i in range(len(prices)):
        tmp_price = prices[i]
        time = 0
        if i == len(prices) - 1:
            answer.append(time)
            break
        for j in range(i+1, len(prices)):
            time += 1
            if tmp_price > prices[j]:
                answer.append(time)
                break
            if j == len(prices) - 1:
                answer.append(time)
    return answer