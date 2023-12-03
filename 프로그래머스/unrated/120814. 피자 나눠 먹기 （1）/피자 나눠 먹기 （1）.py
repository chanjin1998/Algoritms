def solution(n):
    answer = 0
    if n // 7 == n / 7:
        return n//7
    else:
        return n//7 + 1
