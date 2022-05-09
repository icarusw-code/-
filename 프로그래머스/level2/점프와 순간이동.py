def solution(n):
    ans = 0

    while n > 0:
        p, q = divmod(n, 2)
        n = p 
        if q != 0:
            ans += 1

    return ans