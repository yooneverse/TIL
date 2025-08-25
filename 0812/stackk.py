
# 화살표 말고 탭으로 괄호 빠져나와짐
# stack = []
# stack.append(1)
# stack.append(2)
# stack.append(3)
#
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
#
# top = -1
# stack = [0] * 10
#
# top += 1 #push(1)
# stack[top] = 1
# top += 1 #push(1)
# stack[top] = 2
# top += 1 #push(1)
# stack[top] = 3
#
# top -= 1 #pop()
# print(stack[top+1])
# top -= 1 #pop()
# print(stack[top+1])
# top -= 1 #pop()
# print(stack[top+1])

# 파이썬에서 리스트의 메서드를 사용하는 방법

# 빈 리스트를 만들고 이 리스트를 스택처럼 쓰겠다고 정함
s = []

#스택에 원소 삽입 : push
for i in range(10):
    s.append(i) # 리스트의 append() 메서드를 통해 마지막에 추가

print(s)

print(s[-1])
#
# for i in range(10):
#     print(s.pop(), end=',')

# s 안에 뭔가 남아있다면 반복이 계속됨
#s 안에 아무것도 없으면 반복 중단
while s:
    print(s.pop(), end=',')
print()
print(s)