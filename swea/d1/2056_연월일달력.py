t = int(input())
M=[31,28,31,30,31,30,31,31,30,31,30,31]
for test_case in range(1, t+1):
    day = input()
    y = day[:4]
    m = day[4:6]
    d = day[6:]

    if 0 < int(m) < 13 and int(d) <= int(M[int(m) - 1]):
        print(f"#{test_case} {y}/{m}/{d}")
    else:
        print(f"#{test_case} -1")