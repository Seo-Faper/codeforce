# 스도쿠 

'''
0 3 5 4 6 9 2 7 8
7 8 2 1 0 5 6 0 9
0 6 0 2 7 8 1 3 5
3 2 1 0 4 6 8 9 7
8 0 4 9 1 3 5 0 6
5 9 6 8 2 0 4 1 3
9 1 7 6 5 2 0 8 0
6 0 3 7 0 1 9 5 2
2 5 8 3 9 4 7 6 0

>  확정 지을 수 있는 값을 찾는다.
한 행에 0이 하나 뿐인 경우 
한 열에 0이 하나 뿐인 경우
한 3x3에 0이 하나 뿐인 경우 
45-'범위의 모든 합'을 0 자리에 집어 넣는다.


'''

board = [list(map(int,input().split())) for i in range(9) ]
