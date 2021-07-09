pos = input()
pos = [ord(pos[0]) - 96, int(pos[1])]
L = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

print(len([0 for i in L if((0 < pos[0] - i[0] < 9) and (0 < pos[1] -  i[1] < 9))]))