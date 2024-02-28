T = int(input())
for _ in range(T):
    _ = input()  # No need to use this input directly.
    l = list(map(int, input().split()))
    sum_array = sum(l)
    ans = 0
    if  sum_array % 3 == 0:
        print(0)
    if len(l) == 1:
        print(1)
    else:
        mod = [x%3 for x in l ]
        sum_mod = sum(mod)
        # print(mod,sum_mod)
        e = sum_mod % 3
        
        if e == 1:
            tmp = 3 + (sum_mod - 1)
            flag = True
            for i in mod:
                if i == 1:
                    flag = False
                    print(min(tmp,1))
                    break
            if flag:
                print(min(tmp,2))
        else:
            tmp = sum_mod + 1
            print(1)
