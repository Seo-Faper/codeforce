import sys
input = sys.stdin.readline
N = int(input())
pos = [list(map(int, input().split(" "))) for _ in range(N)]

pos.sort(key=lambda x: (x[0], x[1]))

currStart = pos[0][0]
currEnd = pos[0][1]
ans = currEnd - currStart
for i in range(1, N):
    nextStart = pos[i][0]
    nextEnd = pos[i][1]
    if nextStart <= currEnd:
        if nextEnd > currEnd:
            ans += nextEnd - currEnd
            currEnd = nextEnd
    else:
        ans += nextEnd - nextStart
        currEnd = nextEnd
        currStart = nextStart

print(ans)
