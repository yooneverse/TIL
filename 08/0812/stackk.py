#
# stack = []
# stack.append(1)
# stack.append(2)
# stack.append(3)
#
# print(stack.pop())
# print(stack.pop()) # 화살표 말고 탭으로 괄호 빠져나와짐
# print(stack.pop())

top = -1
stack = [0] * 10

top += 1 #push(1)
stack[top] = 1
top += 1 #push(1)
stack[top] = 2
top += 1 #push(1)
stack[top] = 3

top -= 1 #pop()
print(stack[top+1])
top -= 1 #pop()
print(stack[top+1])
top -= 1 #pop()
print(stack[top+1])