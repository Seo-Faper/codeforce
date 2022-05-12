def f(c, t):
    arr = [[0 for _ in range(c+1)] for _ in range(t+1)]
    for i in range(1,t+1):
        for j in range(1,c+1):
           if size[i-1] > j: 
               arr[i][j] = arr[i-1][j]
           else:
               arr[i][j] = max(value[i-1]+arr[i-1][j-size[i-1]],arr[i-1][j])
    return arr[t][c]

n = int(input())
size = list(map(int, input().split(" ")))
value = list(map(int, input().split(" ")))
print(f(99,n))