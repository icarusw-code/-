import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    word = input()
    arr = [i for i in word]
    answer = "Yes"
    if len(set(arr)) == 2:
        for i in set(arr):
            if arr.count(i) == 2:
                continue
            else:
                answer = "No"
    else:
        answer = "No"

    print(f"#{tc} {answer}")
