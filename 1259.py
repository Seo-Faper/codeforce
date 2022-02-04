while True:
    l = input()
    if l == "0": break
    if l == l[::-1]: print("yes")
    else: print("no")
    