def solution(sizes):
    w = 0
    h = 0
    
    for i, j in sizes:
        if i < j:
            i, j = j, i
        w = max(w, i)
        h = max(h, j)
        
    return w * h