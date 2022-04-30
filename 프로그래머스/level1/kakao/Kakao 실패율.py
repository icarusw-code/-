def solution(N, stages):
    answer = [] 
    total = len(stages)
    
    for i in range(1, N+1):
        count = stages.count(i)
        if count == 0:
            fail = 0
        else:
            fail = count / total
        answer.append((i, fail))
        total -= count
    answer = sorted(answer, key=lambda x:x[1], reverse= True)
    answer = [i[0] for i in answer]
    return answer