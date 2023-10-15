def solution(s):
    sum = 0
    for i in s:
        if i == 'p' or i == 'P':
            sum += 1
        elif i == 'y' or i == 'Y':
            sum -= 1
    if sum == 0:
        return True
    else:
        return False
