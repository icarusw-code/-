def solution(nums):
    answer = 0
    new_num = list(set(nums))
    
    if len(nums)//2 >= len(new_num):
        return len(new_num)
    else:
        return len(nums)//2
    
