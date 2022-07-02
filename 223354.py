n = int(input())
stone = input()
L = list(map(int, input().split()))

for i in range(n):
    a = []
    for j in range(i,len(L)):
        if stone[i] == stone[j]:
            a.append(L[i])
        else: break
    print(a,max(a))