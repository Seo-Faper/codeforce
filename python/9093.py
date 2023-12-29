def f(s): return s[::-1]
[print(*i) for i in [ list(map(f,input().split(" "))) for _ in range(int(input()))]]