T = int(input())
for _ in range(T):
    s = input()
    N = int(len(s)**0.5)
    for j in range(N):
        for i in range(N,len(s)+1,N):
            print(s[i-j-1],end='')
    print()