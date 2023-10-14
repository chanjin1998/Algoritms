def solution(n):
    answer = []
    n = str(n)
    answer = ','.join(n)
    result = []
    answer = list(map(int,answer.split(',')))
    for i in answer:
        result.insert(0,i)
    return result