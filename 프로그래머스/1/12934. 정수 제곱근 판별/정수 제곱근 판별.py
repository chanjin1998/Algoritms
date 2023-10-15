import math
def solution(n):
    answer = 0
    alpha = int(pow(n,0.5))
    if pow(alpha,2) == n:
        answer = pow(alpha+1,2)
    else:
        answer = -1
    return answer