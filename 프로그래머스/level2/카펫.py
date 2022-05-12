def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    for x in range(1, total + 1):
        if (total / x) % 1 == 0:
            y = total / x   
            if x >= y:
                if 2*x + 2*y == brown + 4:
                    return[x,y]
    
    return answer