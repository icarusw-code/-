# 90 도 회전
# 1 2 3     7 4 1
# 4 5 6 ==> 8 5 2
# 7 8 9     9 6 3
arr = [[1,2,3], [4,5,6], [7,8,9]]
rotated = list(zip(*arr[::-1]))

print(rotated)

# 전치
transposed = list(zip(*arr))

print(transposed)