hh,mm,ss = map(int,(input().split(':')))
HH,MM,SS = map(int,(input().split(':')))

now_time=(hh*3600)+(mm*60)+ss
start_time=(HH*3600)+(MM*60)+SS
result=start_time-now_time
remain_hh= result//3600
remain_hh2=result%3600
remain_mm=remain_hh2//60
remain_ss=remain_hh2%60

print(f"{remain_hh:0>2}:{remain_mm:0>2}:{remain_ss:0>2}")