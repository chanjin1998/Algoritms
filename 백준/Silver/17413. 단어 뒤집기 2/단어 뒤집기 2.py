import sys
alphas = sys.stdin.readline()
stack = []
tmp = []
answer = ""
for alpha in alphas:
  if alpha == "<":
    while stack:
      answer += stack.pop()
    tmp.append(alpha)
    answer += alpha
  elif alpha.isalpha() or alpha.isdigit():
    if tmp:
      answer += alpha
    else:
      stack.append(alpha)
  elif alpha == " ":
    if len(tmp) == 0:
      while stack:
        answer += stack.pop()
    answer += alpha

  elif alpha == ">":
    tmp.pop()
    answer+= alpha
while stack:
  answer += stack.pop()
print(answer)
    