t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr = sorted(arr)

    print(str(arr[0]) + " " + str(arr[-1]))

