for a in range(1,400):
    for b in range(1,400):
        for c in range(1,400):
            if a**2 + b**2 == c**2 and a+b+c==400:
                print(a,b,c)