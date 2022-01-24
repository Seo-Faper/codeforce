# N-Queen
'''
      0 1 2 3
    0 Q # Q #
    1 # # # #
    2 # Q # #
    3 # # # Q
   
   1번째 퀸은 q[0] = 1 
   2번째 퀸운 q[0] = 2 (덮어써짐)
   이라 했을 때 인덱스가 겹치면 바로 탈락 (같은 행에 있기 때문에)
   > [2,1,3] (n개가아니므로 탈락)

      0 1 2 3
    0 Q # # #
    1 # # Q #
    2 Q # # #
    3 # # # Q

    > [0,2,0,3] 중복되는 값이 있으므로 탈락

    즉, [0,1,2,3] 으로 초기화 하고 모든 경우의 수를 돌면서 조건에 만족하는 배열을 찾기만 하면됨
    서로다른 n명을 1줄로 세우는 경우의 수는 n! 
     
     0 1 2 3
    [1,2,3,0]
    >
      0 1 2 3
    0 # Q # #
    1 # # Q #
    2 # # # Q
    3 Q # # #

    대각선에 있으므로 탈락


   

      0 1 2 3
    0 Q # # #
    1 # # Q #
    2 # Q # #
    3 # # # Q
  
    > 
      0 1 2 3
     [0,2,1,3]
      0,q[0](0)  에 대하여
      1,q[1](2)  대각선인가? no
      2,q[2](1)  대각선인가? no
      3,q[3](3)  대각선인가? yes 탈락 

    index에 1을 더하고 value에 1을 더해는데 비교하는에의 value와 같으면 대각선에 있다. 
    abs(v-i) 가 비교하려는 abs(v-i)랑 같으면 대각선에 있다고 본다.

   ..근데 최대 15니까 15!를 시작부터 만들어 놓고 맞는거만 고르는건 무조건 시간초과가 난다.
   정답인 배열을 하나씩 붙여서 만들어야 할거 같다. 0,1 까지만 만들어도 무조건 대각선에 있으니까 탈락인 것 처럼
   [0], [0,1] (탈락) [0,2], [0,2,1] (탈락) [0,2,3](탈락) [0,2,4] 뭐 이런 식으로 해야 하지 않을까
    
'''
import sys
n = int(sys.stdin.readline().replace("\n", ""))
ans = 0
board = [0]*15

def rule(index):
  for i in range(index):
    if board[index] == board[i] or index-i == abs(board[index]-board[i]):
      return False
  
  return True

def n_queen(index):
  global ans
  if index == n: 
    ans+=1
    return
  for i in range(n):
    board[index] = i
    if rule(index):
      n_queen(index+1)

n_queen(0)
print(ans)