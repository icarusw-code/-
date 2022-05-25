import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    commands = list(list(map(int, input().split())) for _ in range(n))

    answer = 0
    speed = 0
    for command in commands:
        if command[0] == 0:
            answer += speed
        else:
            c, v = command
            if c == 1:
                speed += v
            else:
                if speed <= v:
                    speed = 0
                else:
                    speed -= v
            answer += speed

    print(f"#{tc} {answer}")
