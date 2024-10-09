import sys

con = sys.stdin.readline()
stack = []
answer = ""
for i in con:
  if i.isalpha():
    answer+= i
  elif i == "(":
    stack.append(i)
  elif i == "*" or i == "/":
    while stack and (stack[-1] == "/" or stack[-1] == "*"):
      answer += stack.pop()
    stack.append(i)
  elif i == "+" or i == "-":
    while stack and stack[-1] != "(":
      answer += stack.pop()
    stack.append(i)
  elif i == ")":
    while stack and stack[-1] != "(":
      answer += stack.pop()
    stack.pop()
while stack:
  answer += stack.pop()
print(answer)