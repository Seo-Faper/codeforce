for i in range(int(input())):
   ans =  [ input().split(' ') for _ in range(int(input()))]
   ans.sort(key=lambda x:int(x[0]), reverse=True)
   print(ans[0][1])