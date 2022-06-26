# 3
# 3 2 1
'''



'''

n = int(input())
flag = True
R = []
ans = []
count = 0
for i in range(n):

    user = int(input())

    while user > count:
        
        ans.append("+")
        count+=1
        R.append(count)
    if R[-1] == user:
        R.pop()
        ans.append("-")
    else:
        flag = False

if flag:
    for i in ans:
        print(i)
else:
    print("NO")