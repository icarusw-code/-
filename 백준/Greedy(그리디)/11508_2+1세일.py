n = int(input())
arr = list(int(input()) for _ in range(n))
answer = sum(arr)

arr.sort(reverse=True)

for i in range(2, n, 3):
    answer -= arr[i]

print(answer)