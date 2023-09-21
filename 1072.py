x, y = map(int,input().split())
iz = str(y/x)[:4]
if len(iz)==3:
    iz+='0'
count = 0
mid = x - y
if x == y:
    print(-1)
    exit(-1)
while True:
    mid //=2
    # print(mid)
    init = str((y+mid)/x)[:4]
    print(init, mid)
    if iz == init: break