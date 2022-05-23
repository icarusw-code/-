t = int(input())
for tc in range(1, t+1):
    arr = list(map(int, input().split()))
    answer = 0
    for i in arr:
        if i % 2 == 0:
            continue
        else:
            answer += i
    print("#{0} {1}".format(tc, answer))



