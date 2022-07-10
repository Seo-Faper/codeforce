import sys
ans = []
while True:
    s = sys.stdin.readline().replace("\n","")
    if s =='.':
        break 
    stack = []
    
    for i in s:
        if i == '(' or i =='[':
            stack.append(i)
        elif stack and i == ')' and stack[-1] == '(':
            stack.pop()
        elif stack and i ==')' and stack[-1] =='[':
            stack.append(i)
        elif stack and i == ']' and stack[-1] =='[':
            stack.pop()
        elif stack and i == ']' and stack[-1] =='(':
            stack.append(i)
        elif not stack and i ==')' or i ==']':
            stack.append(i)
      
    if stack:
        ans.append("no")
    else:
        ans.append("yes")

for i in ans:
    print(i)
