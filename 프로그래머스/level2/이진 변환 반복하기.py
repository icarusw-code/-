def solution(s):
    answer = []
    cnt = 0
    zero_count = 0
    
    while(int(s) > 1):
        zero_count += s.count("0")
        s = bin(len(s) - s.count("0"))[2:]
        cnt += 1
    
    answer.append(cnt)
    answer.append(zero_count)
    
    return answer