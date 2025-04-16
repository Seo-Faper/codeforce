import random
import os
import time

players = [
    "jjangjay",
    "red3015",
    "seolheun36",
    "ksd8986",
    "ljw1105",
    "hannattp",
    "gumdong1030",
    "gpt4404",
    "wldn0829",
    "minn0701",
    "djssjssl",
    "yahho2468",
    "oneorz3601"
]
players = ['이현수','김동욱','다시']

print("\n랜덤 룰렛 시작!\n")
time.sleep(1)

for i in range(30):  # 30번 반복
    current = random.choice(players)
  
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("\033[1;32m" + "★ 랜덤 룰렛 ★" + "\033[0m")
    print("\n")
    print("\033[1;33m" + f"   {current}" + "\033[0m")
    
  
    time.sleep(0.1 + i * 0.005)

os.system('cls' if os.name == 'nt' else 'clear')
winner = random.choice(players)
print("\033[1;32m" + "★ 최종 선택 ★" + "\033[0m")
print("\n")
print("\033[1;31m" + f"   {winner}" + "\033[0m")
print("\n축하합니다!")
