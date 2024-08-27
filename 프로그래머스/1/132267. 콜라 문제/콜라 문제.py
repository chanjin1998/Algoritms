def solution(a, b, n):
    answer = 0
    cnt = 0
    while n + cnt >= a:
        if (n) % a == 0:
            answer += (n) // a * b
            n = n // a * b
        else:
            tmp = cnt + n
            answer += tmp // a * b
            cnt = tmp % a
            n = tmp // a * b
        print(answer,n,cnt)
    return answer