import sys
sys.stdin = open("input.txt")

n = int(input())
arr = ["3", "6", "9"]

for i in range(1, n+1):
    count = 0
    for j in str(i):
        if j in arr:
            print("-", end="")
            count = 1
    if count == 0:
        print(i, end=" ")
    if count == 1:
        print(end=" ")



