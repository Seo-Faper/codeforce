'''
7

동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4

오른쪽 1, 왼쪽 2, 아래 3, 위 4 

7
4 50
2 160
3 30
1 60
3 20
1 100


// 입력
1
1 1
4 10
2 10
3 1
1 9
3 9

// 정답
19
 
1
2 50
3 100
1 30
3 60
1 20
4 160

'''

n = int(input())

Value = []
L = []
R = []
for i in range(6):
   a,b = map(int,input().split())

   Value.append(b)
   if a == 1 or a==2: L.append(b)
   else : R.append(b)

hight = max(R)
width = max(L)


ans = []

Value.insert(0,Value[len(Value)-1])
Value.append(Value[1])

for i in range(1,7):
   if Value[i-1]+Value[i+1]==hight or Value[i-1]+Value[i+1]==width:

      ans.append(Value[i])

print(n*(width*hight - (ans[0]*ans[1])))