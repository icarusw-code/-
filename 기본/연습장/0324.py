n = int(input())
arr = list(map(int, input().split()))

result = [0] * n 
used = [0] * len(arr)

# 순열
# def per(lev):
#     if lev == n:
#         print(*result);
#         return
#     for i in range(len(arr)):
#         if used[i] == 1:
#             continue
#         result[lev] = arr[i]
#         used[i] = 1
#         per(lev+1)
#         used[i] = 0

# per(0)


#조합
# def com(lev, start):
#     if lev == n:
#         print(*result)
#         return 
#     for i in range(start, len(arr)):
#         result[lev] = arr[i]
#         com(lev+1, i+1)

# com(0,0)

# 중복 순열
# def r_per(lev):
#     if lev == n:
#         print(*result)
#         return
#     for i in range(len(arr)):
#         result[lev] = arr[i]
#         r_per(lev+ 1)

# r_per(0)