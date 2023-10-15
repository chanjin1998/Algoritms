def solution(n):
    answer = 0
    n = str(n)
    alpha = ','.join(n)
    result = list(map(int,alpha.split(',')))
    result.sort(reverse=True)
    sum = ''
    for i in result:
        sum += str(i)
    return int(sum)