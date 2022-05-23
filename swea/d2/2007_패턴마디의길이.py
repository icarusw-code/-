import sys
sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t+1):
    length = 0
    word = input()
    for i in range(len(word)):
        if word[:i+1] == word[i+1: 2*(i+1)]:
            length = i+1
            break
    print(f"#{tc} {length}")


