def solution(n):
    answer = ""
    tmp = list(str(n))
    tmp.sort(reverse=True)
    
    
    return int(answer.join(tmp))