def binary_search(sorted_list, target):
    left, right = 0, len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid  # 원하는 항목을 찾았을 때 인덱스를 반환
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  

_ = input()
l = [int(x) for x in input().split()]
l.sort()
_ = input()
r = [int(x) for x in input().split()]
for i in r:
    if binary_search(l,i) == -1:
        print(0)
    else:
        print(1)