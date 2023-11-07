def solution(s):
    answer = 0
    def tri(s):
        cnt = 0
        stack = []
        for i in s:
            if i == '[':
                stack.append(i)
            if i == ']':
                if len(stack) == 0:
                    return 0
                else:
                    if stack[-1] != '[':
                        return 0
                    elif stack[-1] == '[':
                        stack.pop()
            if i == '(':
                stack.append(i)
            if i == ')':
                if len(stack) == 0:
                    return 0
                else:
                    if stack[-1] != '(':
                        return 0
                    elif stack[-1] == '(':
                        stack.pop()
            if i == '{':
                stack.append(i)
            if i == '}':
                if len(stack) == 0:
                    return 0
                else:
                    if stack[-1] != '{':
                        return 0
                    elif stack[-1] == '{':
                        stack.pop()
        if len(stack) == 0:
            cnt += 1
        else:
            pass
        return cnt
    for i in range(len(s)):
        s+=s[0]
        s = s[1:len(s)+1]
        answer += tri(s)
    return answer
