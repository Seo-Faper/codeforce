n = int(input())

a = [False,False] + [True]*(n-1)
data=[]

for i in range(2,n+1):
  if a[i]:
    data.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False


T = len(data)
m = n

count = 0
interval_sum = 0
end = 0

 
# start를 차례대로 증가시키며 반복
for start in range(T):
    # end만큼 이동시키기
    while interval_sum < m and end < T:
        interval_sum += data[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]
 
print(count)
