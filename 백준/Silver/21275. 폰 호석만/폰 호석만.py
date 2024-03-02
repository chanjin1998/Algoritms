import sys
input = sys.stdin.readline
A, B = input().split()
x, a, b = 0, 0, 0 # 출력할 값
count = 0 # 조건에 맞는 값이 몇개인지 카운팅해주는 변수


# 1. A를 가지고 2부터 36진수 중 표현이 가능한 값을 찾음
for i in range(2, 37):
    try:
        a_temp = int(A, i)
    except:
        continue
    # 2. B를 가지고 2부터 36진수 중 표현이 가능한 값을 찾음
    for j in range(2, 37):
        try:
            b_temp = int(B, j)
            # 3. 진수 변환한 값들이 같을 떄
            if a_temp == b_temp:
                count += 1
                x = a_temp
                a = i
                b = j
        except:
            continue

# 4. 출력하기
if count == 1:
    if x >= pow(2,63) or x<0 or a==b:
      print("Impossible")
    else:
      print(x,a,b)
elif count == 0:
    print("Impossible")
else:
    print("Multiple")