n = int(input())
ans = [0]*5
for i in range(n):
    x,y = map(int,input().split())
    if x == 0 or y == 0: ans[4]+=1
    elif x > 0 and y > 0: ans[0] +=1
    elif x > 0 and y < 0: ans[3]+=1
    elif x < 0 and y < 0: ans[2]+=1
    else: ans[1]+=1

print("Q1: "+str(ans[0]))
print("Q2: "+str(ans[1]))
print("Q3: "+str(ans[2]))
print("Q4: "+str(ans[3]))
print("AXIS: "+str(ans[4]))