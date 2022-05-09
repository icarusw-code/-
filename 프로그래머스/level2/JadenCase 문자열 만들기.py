def solution(s):
    answer = ''

    s = list(s.split(" "))
    
    for i in s:
        i = i.capitalize()
        answer += (" "+ i)
        
    return answer[1:]