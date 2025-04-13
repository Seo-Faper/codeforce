import sys
input = sys.stdin.readline

N, M = map(int, input().split())
total_weeks = M // 7  # 관찰 기간의 주차 수 (0-indexed로 처리할 예정)
vtuber = {}

def time_convert(s):
    hh, mm = map(int, s.split(":"))
    return hh * 60 + mm

for _ in range(N):
    name, day_str, stime, etime = input().split()
    day = int(day_str)
    runtime = time_convert(etime) - time_convert(stime)
    # 0부터 시작하는 주차 인덱스 계산 (JavaScript의 Math.floor((day-1)/7)와 동일)
    w = (day - 1) // 7  
    # 아직 해당 vtuber가 등록되지 않았다면, 관찰 기간 전체 주에 대한 [방송횟수, 총시간] 리스트 초기화
    if name not in vtuber:
        vtuber[name] = [[0, 0] for _ in range(total_weeks)]
    # 해당 주에 방송 이벤트 개수 증가 및 시간 누적 (각 이벤트 별로 집계)
    vtuber[name][w][0] += 1  
    vtuber[name][w][1] += runtime

answer = []
for name, weeks in vtuber.items():
    qualifies = True
    for week_data in weeks:
        # 각 주마다 방송 횟수가 5회 이상이어야 하고, 총 방송 시간이 3600분 이상이어야 함
        if week_data[0] < 5 or week_data[1] < 3600:
            qualifies = False
            break
    if qualifies:
        answer.append(name)

if not answer:
    print(-1)
else:
    answer.sort()
    print('\n'.join(answer))
