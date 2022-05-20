from itertools import permutations

n = int(input())
arr = list(list(map(int, input().split())) for _ in range(n))

all_list = list(permutations(range(1, 10), 3))

for test in arr:
    q, s, b = test
    removed = 0
    q = list(str(q))

    for i in range(len(all_list)):
        scount, bcount = 0, 0
        i -= removed
        for j in range(3):
            q[j] = int(q[j])
            if q[j] in all_list[i]:
                if j == all_list[i].index(q[j]):
                    scount += 1
                else:
                    bcount += 1
        if scount != s or bcount != b:
            all_list.remove(all_list[i])
            removed += 1
            
print(len(all_list))



