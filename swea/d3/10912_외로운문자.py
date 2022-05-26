import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    word = [i for i in input()]
    stack = []
    word.sort()

    for i in word:
        if len(stack) == 0 or stack[-1] != i:
            stack.append(i)
        else:
            stack.pop(-1)

    if len(stack) == 0:
        print(f"#{tc} Good")
    else:
        tmp = "".join(stack)
        print(f"#{tc} {tmp}")
