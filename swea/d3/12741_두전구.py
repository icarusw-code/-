t = int(input())
tmp = []
for tc in range(1, t+1):
    a, b, c, d = map(int, input().split())
    light1 = [i for i in range(a, b)]
    light2 = [i for i in range(c, d)]

    answer = 0
    for i in light1:
        for j in light2:
            if i == j:
                answer += 1
    tmp.append(f"#{tc} {answer}")
    
print("\n".join(tmp))
