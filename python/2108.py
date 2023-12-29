import sys
import operator

def mode(L):
    count = {}
    for i in L:
        try: count[i] += 1
        except: count[i]=1

    ans = sorted(count.items(), key=operator.itemgetter(1), reverse=True)


    if len(ans) > 1 and ans[0][1] == ans[1][1]:
        return ans[1][0]
    else:
        return ans[0][0]

n = int(sys.stdin.readline())

l = []

for i in range(n):
    l.append(int(sys.stdin.readline()))


l.sort()

print(round(sum(l)/n))
print(l[n//2])
print(mode(l))
print(l[n-1]-l[0])