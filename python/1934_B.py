

T = int(input())
for _ in range(T):
    n = int(input())
    count = 0

    coin_types = [15, 10, 6, 3, 1]
    ans = []
    for coin in coin_types:
        count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
        n %= coin
        
    print(count)