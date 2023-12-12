def solution(array):
    answer = 0
    array.sort()
    return array[int(len(array)/2)]