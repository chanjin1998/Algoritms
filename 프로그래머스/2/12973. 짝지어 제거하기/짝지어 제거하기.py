def solution(s):
    stack = []
    for i in range(len(s)):
        if i == 0:
            stack.append(s[i])
        elif len(stack) != 0:
            if stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])
    if len(stack) == 0:
        return 1
    else:
        return 0
        