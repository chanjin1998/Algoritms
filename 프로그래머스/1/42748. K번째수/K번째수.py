def solution(array, commands):
    answer = []
        
    for arr in commands:
        first_idx = arr[0]
        last_idx = arr[1]
        target_idx = arr[2]
        
        new_arr = array[first_idx-1:last_idx]
        new_arr.sort()
        answer.append(new_arr[target_idx-1])
    return answer