n = int(input())
k = int(input())

senseor = list(map(int, input().split()))
senseor.sort()

tmp = []
for i in range(1, n):
    tmp.append(senseor[i] - senseor[i-1])

tmp.sort()
print(sum(tmp[:n-k]))
