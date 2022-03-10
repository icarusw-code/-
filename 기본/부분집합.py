# 부분집합
n = int(input())

arr = list(map(int, input().split()))

result = [0] * n

def subset(lev, ss):
    if lev == n:
        if not ss:
            return
        print(ss)
        return
    subset(lev + 1, ss + [arr[lev]])
    subset(lev + 1, ss)

subset(0, [])
