from math import ceil
def solution(progresses, speeds):
    answer = []
    left = list(map(lambda x: (ceil((100-progresses[x]) / speeds[x])), range(len(progresses))))
    
#     for i in range(len(progresses)):
#         if (100 - progresses[i]) % speeds[i] == 0:
#             left.append((100-progresses[i]) // speeds[i])
#         else:
#             left.append((100-progresses[i]) // speeds[i] + 1)
            
    
    
    max = left[0]
    cnt = 1
    
    for i in range(1, len(left)):
        if max < left[i]:
            max = left[i]
            answer.append(cnt)
            cnt = 1
        else:
            cnt += 1
            
        if i == len(left) - 1: 
            answer.append(cnt)
        
    return answer