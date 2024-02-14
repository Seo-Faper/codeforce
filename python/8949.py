a,b = map(str,input().split())
ans = []
if len(a) > len(b):
    b = b.zfill(len(a))
else:
    a = a.zfill(len(b))
    
for i in reversed(range(len(a))):
   ans.append(str(int(a[i]) + int(b[i])))
print(''.join(reversed(ans)))
