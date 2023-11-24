def solution(s):
    result = []
    word_list = s.split(' ')
    #A-Z 65-90, a-z 91-126
    for word in word_list:
        answer = ''
        for i in range(len(word)):
            if i % 2 == 0:
                answer += word[i].upper()
            else:
                answer += word[i].lower()
        result.append(answer)     
    return ' '.join(result)