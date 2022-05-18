n = int(input())
arr = []
people = 0

for i in range(n):
    x, a = map(int, input().split())
    arr.append([x, a])
    people += a

arr.sort(key = lambda x:x[0])

count = 0
answer = 0
for i in range(n):
    count += arr[i][1]
    if count >= people/2:
        answer = arr[i][0]
        break

print(answer)