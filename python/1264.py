import sys
k = ['a', 'e', 'i', 'o', 'u']

while True:
    ans  = 0
    t = sys.stdin.readline().replace("\n", "")
    s = t.lower()
    print(s)
    if s == '#': break
    for i in s:
        if i in k  : ans+=1
    print(ans) 
