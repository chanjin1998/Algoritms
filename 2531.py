import sys
n,d,k,c = map(int,sys.stdin.readline().split())
plate = []
max_sushi = 0
for _ in range(n):
  plate.append(int(sys.stdin.readline()))
for i in range(n):
    if i <= n-k:
        tmp = set(plate[i:i+k])
    else:
        tmp = set(plate[i:])
        tmp.update(plate[:(i+k)%n])  # %나머지 기호를 잘 사용하자!
    #print(tmp, end=' ')
    tmp.add(c)
    #print(tmp)
    max_sushi = max(max_sushi, len(tmp))
print(max_sushi)

# A = [0]*10000
# start = 0
# # end = n + k -2
# end = 1
# cnt = 0
# A[fish[start]] += 1
# cnt += 1

# while end <= n+k-2:
#   if A[fish[end]] < 1:
#     A[fish[end]] += 1
#     cnt + 1
#     end += 1
#   elif A[fish]