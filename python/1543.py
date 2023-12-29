document = input()
word = input()
ans = len(document) - len(document.replace(word,"")) 
print(ans // len(word))


# print(input().count(input()))