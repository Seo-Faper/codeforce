n = int(input())
for i in range(n):
    size = int(input())
    l = list(map(int, input().split()))
    l.sort()
    left = []
    right = []
    for j in range(size):
        if j % 2 == 0:
            left.append(l[j])
        else:
            right.append(l[j])
    right.reverse()
    # print(left,right)
    array = left + right
    level = abs(array[0] - array[size-1])
    for j in range(1, size):
        level = max(level,abs(array[j] - array[j-1]))
    print(level)