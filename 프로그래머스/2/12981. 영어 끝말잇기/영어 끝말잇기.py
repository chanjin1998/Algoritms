import math
def solution(n, words):
    answer = []
    right = [words[0]]
    for i in range(1,len(words)):
        if words[i] not in right and words[i][0] == words[i-1][-1]:
            right.append(words[i])
        else:
            if (i+1) % n == 0:
                return n,math.ceil((i+1)/n)
            else:
                return (i+1)%n,math.ceil((i+1)/n)
    return 0,0
