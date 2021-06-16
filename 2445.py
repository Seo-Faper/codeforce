n = int(input())
s = ""
for i in range(1,n):
    s += "*"*i
    s +=" "*(2*(n-i))
    s +="*"*i
    print(s)
    s = ""
print("*"*2*n)
for i in reversed(range(1,n)):
    s += "*"*i
    s +=" "*(2*(n-i))
    s +="*"*i
    print(s)
    s = ""