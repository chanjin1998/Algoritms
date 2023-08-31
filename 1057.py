import math
import sys

n, k, l = map(int, sys.stdin.readline().split())
cnt = 0
while True:
    # 둘의 반올림이 같은 경우 whil문 끝내기
    if math.ceil(k) == math.ceil(l):
        break
    # 김지민,임한수/2로 나누고 반올림 한 값 대입
    k = math.ceil(k / 2)
    l = math.ceil(l / 2)
    cnt += 1

print(cnt)
