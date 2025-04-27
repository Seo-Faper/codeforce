def p1019(N):
    
    counts = [0 for _ in range(10)]

    weight = 1
    for step in range(len(str(N))):
        replaced = int(str(N // 10) + "9")
        remaining = replaced - N
        for i in range(len(counts)): counts[i] += (N // 10 + 1) * weight
        for i in range(10-remaining, 10): counts[i] -= weight
        for number in list(str(N)[:-1]):
            number = int(number)
            counts[number] -= remaining * weight

        counts[0] -= weight

        N //= 10
        weight *= 10
    ans = 0
    for i in range(1,10):
        ans += i * counts[i]

    return ans

L,U = map(int,input().split())
print(p1019(U) - p1019(max(0,L-1)))