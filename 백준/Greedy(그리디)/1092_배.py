n = int(input())
crane = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))

crane.sort(reverse = True)
box.sort(reverse = True)

answer = 0 
visited = [0 for _ in range(m)]
count = 0

positions = [0] * n

if box[0] > crane[0]:
    print(-1)
else:
    while count < len(box):
        for i in range(n):
            while positions[i] < len(box):
                if not visited[positions[i]] and crane[i] >= box[positions[i]]:
                    visited[positions[i]] = True
                    positions[i] += 1
                    count += 1
                    break
                positions[i] += 1
        answer += 1
    print(answer)
