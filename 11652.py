n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
dic = {}
for i in l:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

max_count = max(dic.values())
max_count_elements = [key for key, value in dic.items() if value == max_count]
min_element = min(max_count_elements)

print(min_element)
