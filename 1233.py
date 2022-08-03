
from collections import Counter
a,b,c = map(int,input().split())
ans = []
for i in range(1,a+1):
    for j in range(1,b+1):
        for z in range(1,c+1):
            ans.append(i+j+z)

result = Counter(ans)
my_dict = dict(result)
#print(dict(result))
sorted_dict = sorted(my_dict.items(), key = lambda item: item[1],reverse=True)
print(sorted_dict[0][0])