def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for p in range(len(arr1[0])):
                answer[i][j] += (arr1[i][p] * arr2[p][j] )
            
    return answer