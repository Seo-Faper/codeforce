from collections import deque

l = deque([1,2,3,4,5])
print(l.popleft())
l.rotate(-2)
print(l)

print(l.popleft())
l.rotate(3)
print(l)

print(l.popleft())
l.rotate(1)
print(l)
# 음수면 -붙여서 rotate
# 양수면 -붙이고 + 1 한다음 rotate?
