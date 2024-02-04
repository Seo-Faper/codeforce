
s = input()
result = []

for i in range(1,len(s)):

    new_s = s[i:] # 두 번째 뭉탱이 생성
    a = s[:i][::-1] # 첫번째 뭉탱이를 만들고 뒤집음 
    for j in range(1,len(new_s)):
        b = new_s[:j][::-1] 
        c = new_s[j:][::-1]
        result.append(a + b + c)

result.sort()
print(result[0])
