n = int(input())
for i in range(n):
    s = input()
    if s[len(s)//2] != s[len(s)//2-1]: print("Do-it-Not")
    else: print("Do-it")