import imp
from itertools import product

n, k = map(int, input().split())
length = len(str(n))

arr = list(map(str, input().split()))

while True:
    tmp = list(product(arr, repeat=length))
    answer = []

    for i in tmp:
        if int("".join(i)) <= n:
            answer.append(int("".join(i)))
            
    if len(answer) >= 1:
        print(max(answer))
        break
    else:
        length -= 1


