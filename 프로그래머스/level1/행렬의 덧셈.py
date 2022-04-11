def sumMatrix(A,B):
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] += B[i][j]
    return A
    
def solution(arr1, arr2):
    answer = [[]]
    answer = sumMatrix(arr1, arr2)

            
    return answer