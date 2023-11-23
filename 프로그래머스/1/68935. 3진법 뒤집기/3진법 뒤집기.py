def solution(n):
    answer = ''
    while n!= 0:
        answer += str(n%3)
        n = n // 3
#     tmp = int(pow(n,1/3))
#     result = [0 for _ in range(tmp+1)]
#     new_res = []
#     if n <3 :
#         return n
    
#     while n != 0:
#         if n >= pow(3,tmp):
#             n -= pow(3,tmp)
#             result[len(result)-tmp-1] += 1
#         else:
#             tmp -= 1
#     # for i in range(len(result)-1,-1,-1):
#     #     new_res.append(result[i])
#     for i in range(len(result)):
#         answer += pow(3,i) * result[i]
    return int(answer,3)