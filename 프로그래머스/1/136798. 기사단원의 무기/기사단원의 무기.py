def solution(number, limit, power):
    #기사 번호의 약수 개수에 해당하는 공격력
    answer = 0
    temp_val = []
    for i in range(1,number+1):
        odd_num = 0
        for j in range(1,int(pow(i,0.5))+1):
            if i % j == 0:
                if i == j*j:
                    odd_num+=1
                else:
                    odd_num +=2
        temp_val.append(odd_num)
    for val in temp_val:
        if val > limit:
            answer += power
        else:
            answer += val
    return answer