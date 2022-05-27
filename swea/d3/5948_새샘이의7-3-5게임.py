from itertools import combinations
import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    arr = list(map(int, input().split()))
    tmp = set()
    for i in combinations(arr, 3):
        tmp.add(sum(i))
    tmp = sorted(tmp)
    print(f"#{tc} {tmp[-5]}")
    # tmp = set()
    # for i in range(len(arr)):
    #     for j in range(i+1, len(arr)):
    #         for k in range(j+1, len(arr)):
    #             tmp.add(arr[i]+arr[j]+arr[k])
    # tmp = sorted(tmp, reverse=True)
    #
    # print(f"#{tc} {tmp[4]}")