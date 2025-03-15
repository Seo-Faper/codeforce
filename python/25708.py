n,m = map(int, input().split())
park = [ list(map(int,input().split())) for _ in range(n)]

n_sum = []
m_sum = []
for i in range(m):
    tmp = []
    for j in range(n):
        tmp.append(park[j][i])
    m_sum.append(sum(tmp))
for i in range(n):
    n_sum.append(sum(park[i]))
ans = -999_999_999
#print(n_sum, m_sum)
for i in range(n):
    for j in range(i+1,n):
        for p in range(m):
            for q in range(p+1,m):
                s = n_sum[i] + n_sum[j] + m_sum[p] + m_sum[q] - park[i][p] - park[i][q] - park[j][p] - park[j][q]
                w = max((j - i -1),0)
                h = max((q - p - 1) ,0)
                s += w*h

                ans = max(s,ans)

print(ans)