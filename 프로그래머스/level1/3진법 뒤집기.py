def change(n, q):
    base = ''
    
    while n>0:
        n, mod = divmod(n,q)
        base += str(mod)
    
    return base
    
def solution(n):
    answer = 0
    answer = int(change(n, 3), 3)    
    
    return answer