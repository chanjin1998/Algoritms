import sys
N = int(sys.stdin.readline())
arr=[]
result=[]
for i in range(N):
    arr.append(int(sys.stdin.readline()))
    
arr.sort(reverse=True)
         
for i in range(N):
    result.append(arr[i]*(i+1))
print(max(result))

# 입력받은 무게를 내림차순 한 뒤 1번*1, 2번*2, 3번*3 한 것 중 가장 큰 값을 구해준다.