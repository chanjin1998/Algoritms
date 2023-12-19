def solution(my_string):
    answer = 0
    for i in my_string:
        if 65<=ord(str(i))<=122:
            pass
        else:
            answer += int(i)
    return answer