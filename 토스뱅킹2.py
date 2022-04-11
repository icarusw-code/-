money = 4
limit = 10
max_limit = 10
result = [0, 0] # true, false

while money > -1:
    if money < limit and money != 0:
        result[1] += 1
        limit = limit // 2
    # 성공
    if money >limit and money > (limit//2) and money < max_limit:
        result[0] += 1
        money -= limit
        if money > limit//2:
            result[0] += 1
            break
        else: 
            if limit == 1 and money < limit:
                result[1] += 1
                break
            limit = limit//2
            result[1] += 1
    if money >= max_limit:
        result[0] += 1
        break
    if limit == 1 and money == 0:
        result[1] += 1
        break


print(result)