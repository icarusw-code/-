from collections import deque

def solution(priorities, location):
    answer = 0
    tmp = deque([(x, idx) for idx, x in enumerate(priorities)])
    
    while tmp:
        val = tmp.popleft()
        if tmp and val[0] < max(tmp)[0]:
            tmp.append(val)
        else:
            answer += 1
            if val[1] == location:
                break
        
            
    return answer