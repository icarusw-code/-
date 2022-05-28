def com(arr, n):
    result = []

    if n == 0:
        return [[]]
    
    for i in range(0, len(arr)):
        e = arr[i]
        rest_arr = arr[i+1:]
        for c in com(rest_arr, n-1):
            result.append([e] + c)
    return result

test = [1, 2, 3, 4, 5]
n = 3

check = com(test, n)
print(check)