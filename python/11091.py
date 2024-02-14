n = int(input())
alpha1 = [ chr(x+65) for x in range(26)]

for i in range(n):
    s = input()
    temp = ''.join(alpha1)
    for j in s:
        if j.isalpha():
            temp = temp.replace(j.upper(),'')
    if not temp:
        print("pangram")
    else:
        print("missing",temp.lower())