n, k = map(int, input().split())

number = input()
answer = []

for i in number:
    while k>0 and answer and answer[-1] < i:
        answer.pop()
        k -= 1
    answer.append(i)

tmp = "".join(answer[:len(answer) - k])

print(tmp)
