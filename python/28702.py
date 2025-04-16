idx, value = 0, 0 
for i in range(3):
    s = input()
    if s.isnumeric():
        idx = i
        value = int(s)

for i in range(idx,3):
    value+=1

if value % 3 ==0 and value % 5 ==0:
    print("FizzBuzz")
elif value % 3 ==0:
    print("Fizz") 
elif value % 5 ==0:
    print("Buzz") 
else:
    print(value)

