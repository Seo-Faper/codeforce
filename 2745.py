s = input()
t = "FDCBA"
if "-" in s : print(t.index(s[0])-0.3)
elif "+" in s : print(t.index(s[0])+0.3)
else:  print(t.index(s[0])*1.0)