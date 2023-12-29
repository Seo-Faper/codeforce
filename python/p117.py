Command = input()
x = ord(Command[0]) - 101
y = int(Command[1]) - 5
print(x,y)
#         0  1  2  3
chase = [[8, 8, 8, 4], # 0
         [8, 8, 6, 4], # 1
         [8, 6, 4, 3], # 2
         [4, 4, 3, 2]] # 3
poss = {x >= 0 and y >= 0: [x, y], x <= 0 and y >= 0: [-(x+1), y], x <= 0 and y <= 0: [-(x+1), -(y+1)], x >= 0 and y <= 0: [x, -(y+1)]}
print(chase[poss.get(True)[0]][poss.get(True)[1]])