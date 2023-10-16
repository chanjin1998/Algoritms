def solution(s):
    answer = ''
    alpha = s.split(" ")
    print(alpha)
    cnt = 0
    for word in alpha:
        for j in range(len(word)):
            if j == 0 and (97<=ord(word[j])<=128):
                answer += chr(ord(word[j])-32)
                pass
            elif j!=0 and (65<=ord(word[j])<=96):
                answer += chr(ord(word[j])+32)
            else:
                answer += word[j]
        cnt+=1
        if cnt == len(alpha):
            break
        answer += ' '
    return answer