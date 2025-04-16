MAX = 100_000
n,k = map (int, input().split())
vistited = [0] * (MAX+1)
queue = [n]
vistited[n] = 1
while queue:
    x = queue.pop(0)
    if x == k:
        print(vistited[x]-1)
        break
    if x * 2 <= MAX and not vistited[x * 2]:
        queue.append(x * 2)
        vistited[x * 2] = vistited[x]
    if x - 1 >= 0 and not vistited[x - 1]:
        queue.append(x - 1)
        vistited[x - 1] = vistited[x] + 1   
    if x + 1 <= MAX and not vistited[x + 1]:
        queue.append(x + 1)
        vistited[x + 1] = vistited[x] + 1
