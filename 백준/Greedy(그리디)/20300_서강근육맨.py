n = int(input())
arr = list(map(int, input().split()))

tmp = 0
arr.sort()

if n % 2 ==1:
    tmp = arr.pop(-1)

answer = [arr[i] + arr[-i-1] for i in range(n // 2)]
answer.append(tmp)

print(max(answer))
