s = input()
A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

ans = ""
for i in s:
    if i in A:
        ans+=i.lower()
    else:
        ans+=i.upper() 

print(ans)       