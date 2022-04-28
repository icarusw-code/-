def solution(n, lost, reserve):
    answer = 0
    
    real_reserve = set(reserve) - set(lost)
    real_lost = set(lost) - set(reserve)
    
    for i in real_reserve:
        front = i - 1
        back = i + 1
        
        if front in real_lost:
            real_lost.remove(front)
        elif back in real_lost:
            real_lost.remove(back)
    
    return n - len(real_lost)