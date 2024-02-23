import sys

def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2
        if data[mid] > target:
            end = mid - 1
        elif data[mid] < target:
            start = mid + 1
        else:
            return True
    return False
input = sys.stdin.readline
while True:
    n,m = map(int, input().split())
    ans = 0
    if n == 0 and m == 0:
        break
    else:
        array = set([int(input()) for _ in range(n)])
        cd_no = set([int(input()) for _ in range(m)])
    
        for i in cd_no:
            if binary_search(i,array):
                ans+=1
    print(ans)