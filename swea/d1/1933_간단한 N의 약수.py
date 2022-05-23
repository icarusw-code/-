import sys
sys.stdin = open("input.txt")

n = int(input())
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=" ")

