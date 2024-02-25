import sys

input = sys.stdin.readline
while True:
    n,m = map(int, input().split())
    ans = 0
    if n == 0 and m == 0:
        break
    else:
        array = set([int(input()) for _ in range(n)])
        cd_no = set([int(input()) for _ in range(m)])
        for i in array:
            if i in cd_no: ans+=1
    print(ans)