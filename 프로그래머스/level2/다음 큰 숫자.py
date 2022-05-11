def solution(n):
    answer = 0
    check = bin(n).count("1")
    
    n += 1
    while True:
        if bin(n).count("1") == check:
            answer = n
            break
        else:
            n += 1
    
    
    return answer