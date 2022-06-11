L = [False]+[True]*30
for i in range(1,29):
    L[int(input())] = False

for i in range(len(L)):
    if L[i] : print(i)