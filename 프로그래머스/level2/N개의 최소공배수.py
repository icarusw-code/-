def LCM(a, b):
    for num in range(2, a*b+1):
        if num % a == 0 and num % b ==0:
            return num

def solution(arr):
    answer = arr[0]
    
    for i in arr[1:]:
        answer = LCM(answer, i)
        
    
    return answer