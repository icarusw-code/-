import sys
sys.stdin = open("input.txt")

t = int(input())
dic = {1:"A+", 2:"A0", 3:"A-", 4:"B+", 5:"B0", 6:"B-", 7:"C+", 8:"C0", 9:"C-", 10:"D0"}

for tc in range(1, t+1):
    n, k = map(int, input().split())
    scores = list(list(map(int, input().split())) for _ in range(n))
    tmp = []
    for idx, score in enumerate(scores):
        s1, s2, s3 = score
        tmp.append([idx+1, round(s1*0.35 + s2*0.45 + s3*0.2, 2)])

    tmp.sort(key=lambda x:x[1], reverse=True)

    for idx, value in enumerate(tmp):
        if value[0] == k:
            answer = (dic[idx // (n//10) + 1])

    print(f"#{tc} {answer}")
