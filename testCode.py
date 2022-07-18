s = "ABBBBBBCDEF"

q = list(s)
q[0] = ''

s = "".join(q)
print(s)