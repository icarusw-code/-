# 조합
from unittest import result


n = int(input())

arr = list(map(int, input().split()))

result = [0] * n

tmp = []

def com(lev, start):
    if lev == n:
        print(*result)
        return
    for i in range(start, len(arr)):
        result[lev] = arr[i]
        com(lev+1 , i + 1)

com(0, 0)
