def solution(arr):
    ls = sorted(arr)
    if len(arr) == 1:
        return [-1]
    for i in arr:
        if i == ls[0]:
            arr.remove(i)

    
    return arr