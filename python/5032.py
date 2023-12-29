#빈 병의 수 e, 그날 발견한 빈 병의 수 f, 새 병으로 바꾸는데 필요한 빈 병의 개수 c
# 9 0 3 -> 3개 바꿔 먹고 빈병 3개를 다시 1개로 바꿔 총 4개

# 
e,f,c = map(int,input().split())

ans = 0
t = e+f
while True:
    
    t -= c
    if t < 0 : break

    ans+=1
    t+=1
print(ans)