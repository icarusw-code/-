import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    word = input()

    for i in range(len(word)):
        if word[i] != word[len(word) - i -1]:
            print(f"#{tc} 0")
            break
    else:
        print(f"#{tc} 1")

