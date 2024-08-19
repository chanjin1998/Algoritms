import sys
m = int(sys.stdin.readline())
n = m
seed = list(map(int,sys.stdin.readline().split()))

num = 0
fin = 0
p_cnt = 0
m_cnt = 0
c = 0
for i in range(14):
  if m >= seed[i]:
    num += m // seed[i]
    m = m % seed[i]
  if i == 13:
    fin = num * seed[i] + m
for i in range(13):
  if seed[i]<seed[i+1]:
    p_cnt += 1
    m_cnt = 0
  elif seed[i]>seed[i+1]:
    p_cnt = 0
    m_cnt += 1
  elif seed[i] == seed[i+1]:
    p_cnt = 0
    m_cnt = 0
  if p_cnt >= 3 and c != 0:
    n += seed[i+1] * c
    c = 0
  if m_cnt >= 3:
    if n >= seed[i+1]:
      c += n // seed[i+1]
      n = n % seed[i+1]
  if i == 12 and p_cnt <3:
    n += c * seed[13]

if fin > n:
  print("BNP")
elif fin == n:
  print("SAMESAME")
else:
  print("TIMING")