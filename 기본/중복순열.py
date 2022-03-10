# 중복 순열
n = int(input())

arr = list(map(int, input().split()))

result = [0] * n

def r_per(lev):
    if lev == n:
        print(result)
        return
    
    for i in range(len(arr)):
        result[lev] = arr[i]
        r_per(lev + 1)

r_per(0)