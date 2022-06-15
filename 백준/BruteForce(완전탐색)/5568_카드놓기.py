from itertools import permutations

n = int(input())
k = int(input())
arr = []
answer = set()

for _ in range(n):
    arr.append(int(input()))

number = list(permutations(arr, k))

for n in number:
    tmp = ""
    for i in range(k):
        tmp += str(n[i])
    answer.add(int(tmp))

print(len(answer))