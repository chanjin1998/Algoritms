def solution(array, height):
    answer = 0
    for heights in array:
        if heights > height:
            answer += 1
    return answer