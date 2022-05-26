import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    word = [i for i in input()]

    for i in range(len(word)):
        if word[i] == "b":
            word[i] = "d"
        elif word[i] == "d":
            word[i] = "b"
        elif word[i] == "p":
            word[i] = "q"
        elif word[i] == "q":
            word[i] = "p"

    answer = ""
    for i in range(len(word)-1, -1, -1):
        answer += word[i]

    print(f"#{tc} {answer}")
