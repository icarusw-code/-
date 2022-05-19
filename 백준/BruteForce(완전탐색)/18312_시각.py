hh=0 ;mm=0 ;ss=0
cnt=0
n,k=map(int, input().split())
while 1:
    if str(k) in str(hh).zfill(2) or str(k) in str(mm).zfill(2) or str(k) in str(ss).zfill(2):cnt+=1
    if hh == n and mm == 59 and ss == 59: print(cnt);break
    ss+=1
    if ss==60 : mm+=1; ss-=60
    if mm==60 : hh+=1; mm-=60