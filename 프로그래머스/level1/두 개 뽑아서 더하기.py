from itertools import combinations as comb
def solution(numbers):
    answer = set()
    tmp = list(comb(numbers,2))
    
    for t in tmp:
        answer.add(sum(t))
        
    return sorted(answer)