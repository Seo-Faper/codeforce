n = int(input())
answer = 0
w = 2 # 일 : 0, 월 : 1, 화 : 2, 수 : 3, 목 : 4, 금 : 5, 토 : 6
for year in range(2019, n+1):
    is_yoon = False
    if year % 400 == 0 : is_yoon = True
    if year % 400 != 0 and year % 100 == 0: is_yoon = False
    if year % 100 != 0 and year % 4 == 0 : is_yoon = True

    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_yoon: months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    

    for m in months:
        for n in range(1,m+1):
            w %= 7
            if w == 5 and n == 13:
                answer +=1
            w +=1
print(answer)