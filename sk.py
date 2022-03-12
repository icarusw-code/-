# money = 1999
money = 4578
# costs = [2, 11, 20, 100, 200, 600]
costs = [1, 4, 99, 35, 50, 1000]

real =  [1, 5,  10,  50, 100, 500]
used = [0]
result = 0

for i in range(5):
    if costs[i] * (real[i+1] // real[i]) < costs[i+1]:
        continue
    else:
        used.append(i+1)
used.reverse()

for i in used:
    result += (costs[i] * (money // real[i]))
    money = money % real[i]

print(result)
