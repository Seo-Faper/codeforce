s = input()
k = "CHICKENS"

key = 0

while True:
    if ord(s[0]) ^ key == ord("C"):
      #  print(key)
        break
    key+=1

for i in s:
    print(chr(ord(i)^key),end='')