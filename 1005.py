'''
첫째 줄에는 테스트케이스의 개수 T가 주어진다. 각 테스트 케이스는 다음과 같이 주어진다. 

첫째 줄에 건물의 개수 N과 건물간의 건설순서 규칙의 총 개수 K이 주어진다. 
(건물의 번호는 1번부터 N번까지 존재한다) 

둘째 줄에는 각 건물당 건설에 걸리는 시간 D1, D2, ..., DN이 공백을 사이로 주어진다. 
셋째 줄부터 K+2줄까지 건설순서 X Y가 주어진다. 
(이는 건물 X를 지은 다음에 건물 Y를 짓는 것이 가능하다는 의미이다) 

마지막 줄에는 백준이가 승리하기 위해 건설해야 할 건물의 번호 W가 주어진다.



건물 W를 건설완료 하는데 드는 최소 시간을 출력한다. 편의상 건물을 짓는 명령을 내리는 데는 시간이 소요되지 않는다고 가정한다.

건설순서는 모든 건물이 건설 가능하도록 주어진다.


<
1
4 4
10 1 100 10
1 2
1 3
2 4
3 4
4


120

건물 4개
각각 드는 시간 10,1,100,10초
        0 1  2  3  4 
time = [0,10,1,100,10]

그래프 : 

G[1][2]
G[1][3]
G[2][4]
G[3][4]

G
- 0 1 2 3 4
0 0 0 0 0 0
1 0 0 1 1 0
2 0 0 0 0 1
3 0 0 0 0 1
4 0 0 0 0 0

1(10) ㅡ 2(1)
  |  ㄴ 4(10)
  ㄴ 3(100)


  이렇게 연결 되어 있다.
   4로 가는 최소한의 시간은 
   1->3->4 (10+100+10 = 120)
   1->2->4가 안되는 이유는 4를 짓기 위해선 무조건 3이 필요하기 때문에
   1->2->3->4 하면 121이다.
   
   위상 정렬 알고리즘 쓴 다음 차수가 0이 될 때
   DP테이블에 걸리는 시간 넣고 비교해서 같은 우선순위 일 때
   최대로 걸리는 시간 담으면 됨 
   
'''
from collections import deque
import sys




def solution():
    N, K = map(int, sys.stdin.readline().split())
    D = list(map(int, sys.stdin.readline().split()))
    D.insert(0, 0)
    
    V = [0] * (N+1)
    G = [[] for _ in range(N+1)]
    for _ in range(K):
        x,y = map(int, sys.stdin.readline().split())
        G[x].append(y)
        V[y]+=1
    W = int(sys.stdin.readline())

    def topology_sort():
        dp = [0]*(N+1)

        q = deque()

        for i in range(1, N+1):
            if V[i] == 0:
                q.append(i)
                dp[i] += D[i]
        while q:

            now = q.popleft()
            

            for i in G[now]:
                V[i] -=1
                dp[i] = max(dp[i],dp[now]+D[i])
                if V[i] ==0:
                    q.append(i)
        return dp       

        
        

    print(topology_sort()[W])

T = int(input())
for i in range(T):
    solution()


