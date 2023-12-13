def solution(n):
    answer = 0
    if pow(n,0.5) == int(pow(n,0.5)):
        return 1
    else:
        return 2
