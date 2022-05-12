def solution(clothes):
    answer = 1
    dic = {}
    
    for clothe, kinds in clothes:
        dic[kinds] = dic.get(kinds, 0) + 1
    
    for value in dic.values():
        answer *= (value+1)
        
    return answer - 1