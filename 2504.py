import sys

s = sys.stdin.readline()
q = []
tmp = 1
cnt = 0

for i in range(len(s)):
  if s[i] == '(':
    tmp *= 2
    q.append(s[i])
  elif s[i] == '[':
    tmp *= 3
    q.append(s[i])
  elif s[i] == ')':
    if len(q) == 0 or q[-1] == '[':
      cnt = 0
      break
    if s[i-1] == '(':
      cnt += tmp
    q.pop()
    tmp //= 2
  elif s[i] ==']':
    if len(q) == 0 or q[-1] == '(':
      cnt = 0
      break
    if s[i-1] == '[':
      cnt += tmp
    q.pop()
    tmp //= 3

if len(q) == 0:
  print(cnt)
else:
  print(0)






































# q = []
# res = []
# str = ''
# cnt = 0
# q.append(s[0])
# for i in range(1,len(s)):
#   if (s[i-1] == '(' and s[i] == '(') or (s[i-1] == '[' and s[i] == '[') or (s[i-1] == '[' and s[i] == '(') or (s[i-1] == '(' and s[i] == '['):
#     res.append('*')
#   elif (s[i-1] == '(' and s[i] == ')') or (s[i-1] == ']' and s[i] == ')') or (s[i-1] == ')' and s[i] == ')'):
#     res.append(2)
#   elif (s[i-1] == '[' and s[i] == ']') or (s[i-1] == ')' and s[i] == ']') or (s[i-1] == ']' and s[i] == ']'):
#     res.append(3)
#   elif (s[i-1] == ']' and s[i] == '(') or (s[i-1] == ')' and s[i] == '[') or (s[i-1] == ']' and s[i] == '[') or (s[i-1] == ')' and s[i] == '('):
#     res.append('+')
# while (len(res)>0):
#   for i in range(1,len(res)):
#     if len(res)<3:
#       break
#     if (res[i-1] == '*' or res[i-1] =='+') and isinstance(res[i],int) and isinstance(res[i+1],int):

# print(res)
