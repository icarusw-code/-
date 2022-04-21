def solution(id_list, report, k):
    count={x : 0 for x in id_list}
    answer = [0] * len(id_list)
    
    for i in set(report):
        count[i.split()[1]] += 1

    for i in set(report):
        if count[i.split()[1]] >= k:
            answer[id_list.index(i.split()[0])] +=1
        
    return answer