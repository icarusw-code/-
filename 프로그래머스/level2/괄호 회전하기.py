from collections import deque

def check(s):
    stack = []
    for i in s:
        if i =="(" or i=="{" or i=="[":
            stack.append(i)
        else:
            if stack == []:
                return False
            tmp = stack.pop()
            if i == ")" and tmp != "(":
                return False
            elif i == "}" and tmp != "{":
                return False
            elif i == "]" and tmp != "[":
                return False
    return stack == []

def solution(s):
    answer = 0
    s = deque(s)
    for i in range(len(s)):
        s.rotate(-1)
        if check(s):
            answer += 1

    return answer