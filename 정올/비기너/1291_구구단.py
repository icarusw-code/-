def timetable(n):
    for i in range(1, 10):
        print(n, " * ", i, " = ", n * i)

s, e = list(map(int, input().split()))

while((s < 2) or (s > 9) or (e < 2) or (e > 9)):
    print("INPUT ERROR!")
    s, e = list(map(int, input().split()))
    
if (s > e):
    for i in range(s, e - 1, -1):
        timetable(i)
else: 
    for i in range(s, e + 1):
        timetable(i)

    
