n = int(input())
for i in range(n):
    price = float(input())
    print("$"+format(price - price * 0.2, ".2f") )