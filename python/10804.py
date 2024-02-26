card = [x for x in range(0,21)]
command = [list(map(int,input().split())) for _ in range(10)]
for i in command:
    card = card[:i[0]] + card[i[0] : i[1]+1][::-1] + card[i[1]+1:]
print(*card[1:])