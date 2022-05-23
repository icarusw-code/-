t = int(input())
score = list(map(int, input().split()))
score.sort()

print(score[(t-1)//2])