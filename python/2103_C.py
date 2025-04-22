import sys
input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        if n < 3:
            print("NO")
            continue

        s = [0] * (n+1)
        for i, v in enumerate(a):
            s[i+1] = s[i] + (1 if v <= k else -1) # 누적합 
        total = s[n]
        p_n = n & 1  

        INF = 10**18
       
        min_s_any = [INF, INF]
        min_s_c1 = [INF, INF]
        earliest = [False, False]
        p_i = 1
        si = s[1]
        min_s_any[p_i] = si
        if si >= p_i:
            min_s_c1[p_i] = si
            earliest[p_i] = True

        ans = False
        for j in range(2, n):
            sj = s[j]
            p_j = j & 1
            for p_i in (0, 1):
                if earliest[p_i]:           
                    if p_i == p_j:

                        if min_s_c1[p_i] <= sj:
                            ans = True; break
                    else:
                        if min_s_c1[p_i] <= sj - 1:
                            ans = True; break
            if ans:
                print("YES")
                break

            if (earliest[0] or earliest[1]):
                if sj <= total - (p_n ^ p_j):
                    print("YES")
                    ans = True
            if ans:
                break

            if sj <= total - (p_n ^ p_j):
                for p_i in (0, 1):
                    if min_s_any[p_i] < INF:
                        if p_i == p_j:
                            if min_s_any[p_i] <= sj:
                                ans = True; break
                        else:
                            if min_s_any[p_i] <= sj - 1:
                                ans = True; break
                if ans:
                    print("YES")
                    break

            p_i = p_j
            si = sj
            if si < min_s_any[p_i]:
                min_s_any[p_i] = si
            if si >= p_i and si < min_s_c1[p_i]:
                min_s_c1[p_i] = si
                earliest[p_i] = True
        else:
            print("NO")


solve()
