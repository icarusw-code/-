n = 2
arr = [1, 2, 3, 4]

# def com(arr, n):
#     result = []

#     if n == 0:
#         return [[]]
    
#     for i in range(0, len(arr)):
#         e = arr[i]
#         rest_arr = arr[i+1:]
#         for c in com(rest_arr, n-1):
#             result.append([e] + c)

#     return result

# print(com(arr, n))

def per(arr, n):
    result = []

    if n == 0:
        return [[]]
    
    for idx, e in enumerate(arr):
        for p in per(arr[:idx] + arr[idx+1:], n-1):
            result += [[e] + p]
    
    return result