from collections import deque

def convert_time(s) :
    h, m = map(int, s.split(':'))
    return h*60 + m

def solution(plans):
    answer = []
    plans = [ (name, convert_time(start), int(playtime)) for name, start, playtime in plans]
    plans.sort(key = lambda x : x[1])
    q = deque()
    left_time = 0
    sk = []
    print(plans)
    for i in range(len(plans)):
        if i == len(plans)-1:
            sk.append(plans[i])
            break
        curr_name, curr_start, curr_playtime = plans[i]
        next_name, next_start, next_playtime = plans[i+1]
        if curr_start + curr_playtime <= next_start: # 다음 시작 전에 끝낼 수 없는 경우
            #
            pass
        else:
            curr_playtime = curr_playtime - (next_start - curr_start) # 다음 시작 전에 끝낼 수 있는 경우 
            sk.append([curr_name, curr_name, curr_playtime])     
    print(sk)
    return answer
print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))