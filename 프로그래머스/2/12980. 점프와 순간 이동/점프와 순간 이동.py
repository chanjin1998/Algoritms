# 순간이동 건전지 안줌, 점프하면 k만큼 줌, 건전지 사용량 최소
def solution(n):
    cnt  = 0
    while (True):
        if n == 1:
            break
        if n % 2 == 0:
            n = n / 2
        else:
            n = (n-1) / 2
            cnt += 1
            
    # 5000 2500 1250 625 624+1 312 156 78 39 38+1 19 18+1 9 8+1 4 2 1
    

    return cnt+1