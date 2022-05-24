import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = list(list(map(int, input().split())) for _ in range(n))
    arr_90 = []
    arr_180 = []
    arr_270 = []
    for i in range(n):
        for j in range(n):
            arr_90.append(arr[n-j-1][i])
            arr_180.append(arr[n-i-1][n-j-1])
            arr_270.append(arr[j][n-i-1])

    print('#',tc,sep='')
    for i in range(0,n*n,n):
        print(''.join(map(str,arr_90[i:i+n])),''.join(map(str,arr_180[i:i+n])),''.join(map(str,arr_270[i:i+n])))