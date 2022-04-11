n = int(input())
count = 0

if n < 5:
    if n % 2 != 0:
        result = -1 
    else:
        result = n // 2
else:
    count, n = divmod(n, 5)
    if n ==0:
        result = count
    else:
        if n % 2 ==0:
            count += n //2
            result = count
        else:
            count += (n + 5) // 2 - 1
            result = count

print(result)