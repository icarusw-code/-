import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    arr = list(map(int, input().split()))
    arr.sort()
    answer = round(sum(arr[1:len(arr)-1]) / 8)
    print(f"#{tc} {answer}")

