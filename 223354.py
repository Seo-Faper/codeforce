n = int(input())
stone = input()
L = list(map(int, input().split()))

'''
8
B B B W B W B B
6 4 8 4 5 3 1 5

B B B W B W B B
0 0 0 4 5 3 0 0

'''
for i in range(n-1):
    L[i] = 0
    if stone[i] == stone[i+1]:

        L[i+1] = 0
    else: break

for i in reversed(range(1,n)):
    L[i] = 0
    if stone[i] == stone[i-1]:

        L[i-1] = 0
    else: break

L2 = sorted(L,reverse=True)

print(L)
print(L2)

for i in range(len(L2)):
    T = L2[i]
    index = L.index(T)
    print(T,index)
    