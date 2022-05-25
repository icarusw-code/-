import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    day = input()
    arr = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

    answer = arr.index("SUN") - arr.index(day)
    if answer == 0:
        answer = 7
    print(f"#{tc} {answer}")
