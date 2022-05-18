n = int(input())
crains = list(map(int, input().split()))
m = int(input())
boxs = list(map(int, input().split()))

answer = 0
crains.sort(reverse=True)
boxs.sort(reverse=True)

if boxs[0] > crains[0]:
    print(-1)

else:
    while len(boxs) > 0:
        for crain in crains:
            for box in boxs:
                if crain >= box:
                    boxs.remove(box)
                    break
        answer += 1

    print(answer)
