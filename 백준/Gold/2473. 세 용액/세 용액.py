import sys
n = int(sys.stdin.readline())
liquid = list(map(int,sys.stdin.readline().split()))

liquid.sort()
tmp = 3000000000
for i in range(n-2):
  now_val = liquid[i]
  left_p = i + 1
  right_p = n - 1

  while left_p < right_p:
    tmp_sum = now_val + liquid[left_p] + liquid[right_p]
    if abs(tmp_sum) <= abs(tmp) :
      tmp = tmp_sum
      res = [now_val, liquid[left_p], liquid[right_p]]
    if tmp_sum > 0:
      right_p -= 1
    elif tmp_sum < 0:
      left_p += 1
    else:
      print(*res)
      sys.exit()
print(*res)
  