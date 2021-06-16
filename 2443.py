n = int(input())
s = ""
for i in range(0,n):
    s+=" "*i
    s +="*"*(2*(n-i)-1)
    print(s)
    s = ""

