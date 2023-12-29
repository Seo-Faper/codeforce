n = int(input())
data_list = [input() for i in range(n)]

data_list = list(set(data_list))

data_list.sort()
data_list.sort(key=lambda x : len(x))

for i in data_list:
    print(i)
