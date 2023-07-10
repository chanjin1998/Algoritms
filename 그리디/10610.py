import sys
N = int(sys.stdin.readline())
S = sorted(str(N), reverse=True)
cnt = 0
if '0' not in S:
  print(-1)
else:
  for i in S:
    cnt += int(i)
  if cnt % 3 !=0:
    print(-1)
  else:
    print(''.join(S))

#3의 배수인지 0을 포함하는지 그 후 내림차순 정렬, 시간 초과하지 않기 위해서 출력 바로바로