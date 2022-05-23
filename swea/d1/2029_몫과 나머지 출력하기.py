t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    a, b = divmod(n, m)
    print(f"#{tc} {a} {b}")