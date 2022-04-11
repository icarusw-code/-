# contests = [[1,5,2,3],[9,9,9,9],[1,9,3,9],[4,3,2,1]]
# k = 2
# p = 4

contests = [[1,1,1], [2,2,2], [1,1,1]]
k = 2
p = 2

result = [] * k
count = 0
count_list = []

for contest in contests:
    for j in contest:
        if j <= p:
            count += 1
    count_list.append(count)
    count = 0

dict = {i: count_list[i] for i in range(len(count_list))}
dict = sorted(dict.items(), key = lambda x: x[1], reverse=True)

for i in range(k):
    result.append(dict[:k][i][0])

result.sort()
print(result)
