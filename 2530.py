h,m,s = map(int,input().split())
t = int(input())

now = (h*60+m)*60+s+t

print(now//60//60%24,now//60%60,now%60)
