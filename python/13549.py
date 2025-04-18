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
    if x * 2 <= MAX and not vistited[x * 2]: # x*2 is not visited
        queue.append(x * 2) #   add x*2 to the queue
        vistited[x * 2] = vistited[x] #  mark x*2 as visited
    if x - 1 >= 0 and not vistited[x - 1]: # x-1 is not visited
        queue.append(x - 1)     #   add x-1 to the queue
        vistited[x - 1] = vistited[x] + 1       # mark x-1 as visited
    if x + 1 <= MAX and not vistited[x + 1]:    # x+1 is not visited
        queue.append(x + 1)   #   add x+1 to the queue  
        vistited[x + 1] = vistited[x] + 1     # mark x+1 as visited
