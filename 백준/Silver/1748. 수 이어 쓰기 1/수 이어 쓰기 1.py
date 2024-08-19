import sys
n = int(sys.stdin.readline())
tmp = 1
for i in range(9):
  if n // pow(10,i) != 0:
    tmp = i
  elif n // pow(10,i) == 0:
    break
# print(tmp)
cnt = 0
for i in range(tmp + 1):
  if i == tmp:
    cnt += ((n % pow(10,i+1)) - pow(10,i) + 1) * (tmp+1)
  else:
    cnt += (i+1) * pow(10,i) * 9
# 한자릿수 = n
# 두자릿수 = 1 * 9 + 2 * ((n % pow(10,i)) + 1)
# 세자릿수 = 1 * 9 + 2 * 90 + 3 * (n % pow(10,i) + 1)
# 네자릿수 = 1 * 9 + 2 * 90 + 3 * 900
print(cnt)