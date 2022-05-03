answer = 0
def dfs(numbers, target, summ, depth):
    global answer
    
    if len(numbers) == depth:
        if summ == target:
            answer += 1
    
    if depth < len(numbers):
        dfs(numbers, target, summ + numbers[depth], depth+1)
        dfs(numbers, target, summ - numbers[depth], depth+1)



def solution(numbers, target):
    global answer
    dfs(numbers, target, 0, 0)
    
    return answer