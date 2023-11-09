def solution(s):
    answer = ''
    word = ''
    # for i in s:
        
        # print(type(i))
        # if type(i) == 'str':
        #     print(i)
        #     word += i
        #     if word == 'one':
        #         answer += '1'
        #         word = ''
        #     if word == 'two':
        #         answer += '2'
        #         word = ''
        #     if word == 'three':
        #         answer += '3'
        #         word = ''
        #     if word == 'four':
        #         answer += '4'
        #         word = ''
        #     if word == 'five':
        #         answer += '5'
        #         word = ''
        #     if word == 'six':
        #         answer += '6'
        #         word = ''
        #     if word == 'seven':
        #         answer += '7'
        #         word = ''
        #     if word == 'eight':
        #         answer += '8'
        #         word = ''
        #     if word == 'nine':
        #         answer += '9'
        #         word = ''
        # else:
        #     answer += str(i)
    s = s.replace('zero','0')
    s = s.replace('one','1')
    s = s.replace('two','2')
    s = s.replace('three','3')
    s = s.replace('four','4')
    s = s.replace('five','5')
    s = s.replace('six','6')
    s = s.replace('seven','7')
    s = s.replace('eight','8')
    s = s.replace('nine','9')
    return int(s)