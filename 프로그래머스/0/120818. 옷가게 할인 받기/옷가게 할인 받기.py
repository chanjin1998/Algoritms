def solution(price):
    if price >= 500000:
        answer = price * 0.8
        return int(answer)
    elif price >= 300000 and price < 500000:
        answer = price * 0.9
        return int(answer)
    elif price >= 100000 and price < 300000:
        answer = price * 0.95
        return int(answer)
    else:
        return price


