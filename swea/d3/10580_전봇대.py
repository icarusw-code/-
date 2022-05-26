import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = list(list(map(int, input().split()))for _ in range(n))

    answer = 0
    for i in range(n-1):
        for j in range(i+1, n):
            s1, e1 = arr[i]
            s2, e2 = arr[j]
            if (s1 > s2 and e1 < e2) or (s1 < s2 and e1 > e2):
                answer += 1
    print(f"#{tc} {answer}")