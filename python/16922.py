word = [1,5,10,50]
visit = [False] * ( 50 * 20 + 1) #L로 꽉 채운 값 
n = int(input())
ans = 0
result = []
def recur(start,ans, dept):
    if dept == n:
        if not visit[ans]:
            # False면 -> 최초 등장한 수면
            result.append(1)
            visit[ans] = True

        return
    for i in range(start,4):
        recur(i,ans+word[i],dept+1)
recur(0,ans,0)
print(len(result))