def solution(brown, yellow):
    answer = []
    i=3
    while True:
        j = 1
        while i>=j:
            j+=1
            if i*j == brown+yellow:
                if (i-2) * (j-2) == yellow:
                    break
        if i>=j:
            return i,j
        i+=1