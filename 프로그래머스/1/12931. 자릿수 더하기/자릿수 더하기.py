def solution(n):
    answer = 0
    n = str(n)
    result = []
    answer = ','.join(n)
    sum = 0
    result = list(map(str,answer.split(',')))
    print(result)
    for i in result:
        sum += int(i)

    return sum