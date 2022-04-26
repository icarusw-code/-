result = [0] * 3
tmp = []

def com(lev, start, nums):
    if lev == 3:
        tmp.append(list(result))
        return 
    for i in range(start, len(nums)):
        result[lev] = nums[i]
        com(lev+1, i+1, nums)
        
def solution(nums):
    answer = 0
    com(0,0, nums)
    for i in tmp:
        cand = sum(i)
        for j in range(2, cand):
            if cand % j == 0:
                break
        else:
            answer += 1    
    
    return answer





#==================소수 직접 확인 ===================#
def find(number):
    cnt = 0
    for i in range(1, number+1):
        if number % i == 0:
            cnt += 1
    if cnt == 2:
        return True
    else:
        return False

result = [0] * 3
tmp = []

def com(lev, start, nums):
    if lev == 3:
        tmp.append(list(result))
        return 
    for i in range(start, len(nums)):
        result[lev] = nums[i]
        com(lev+1, i+1, nums)
        
def solution(nums):
    answer = 0
    com(0,0, nums)
    for i in tmp:
        if find(sum(i)) == True:
            answer += 1
    
    return answer