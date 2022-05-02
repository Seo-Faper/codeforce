N,M = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)] # NxM 배열 선언과 동시에 입력 받는 코드
print('---')
for i in range(N):
    for j in range(M):
        print(arr[i][j],end=' ')
    print()