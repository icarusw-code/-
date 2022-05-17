from collections import defaultdict

n = int(input())
s = input()

dic = defaultdict(int)

dic[s[0]] += 1

for i in range(1, n):
    if s[i] != s[i-1]:
        dic[s[i]] += 1

answer = min(dic["B"], dic["R"]) + 1

print(answer)