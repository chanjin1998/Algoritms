from collections import deque
def solution(s):
    answer = True
    q = deque()
    for i in s:
        if i == '(':
            q.append(i)
        if i == ')' and '(' not in q:
            return False
        if i == ')' and '(' in q:
            q.pop()
    if len(q) == 0:
        answer = True
    else:
        answer = False
    return answer