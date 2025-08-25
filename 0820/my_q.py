# front = rear = -1
# q = [0] * 10
#
# rear += 1 # enq(1)
# q[rear] = 1
# rear += 1 # enq(2)
# q[rear] = 2
# rear += 1 # enq(3)
# q[rear] = 3
#
# front += 1 # deq()
# print(q[front])
# front += 1 # deq()
# print(q[front])
# front += 1 # deq()
# print(q[front])
#
# #front가 어디까지 갔느냐가 중요한 것

'''
강사님 코드
'''

# 선형큐 2
# front와 rear를 사용

# 큐의 크기
N = 3

# 공백 상태의 큐 생성
q = [0] * N

front = rear = -1
# front : 마지막에 삭제한 원소의 위치
# rear : 마지막에 삽입한 원소의 위치

# 1, 2, 3 삽입
for i in range(1,4):
    # 가장 마지막에 삽입한 원소의 한 칸 뒤에 삽입을 해야 되겠다.
    # 그래서 어떻게 한다??
    rear += 1
    q[rear] = i

print(q)

# 원소 삭제 3번
for i in range(3):
    # 가장 마지막에 삭제한 원소의 위치 +1에 있는 원소를 새로 삭제해준다는 것
    front += 1
    print(q[front], end=",")
print()

print(q, front, rear) # front랑 rear가 같으면 비어있다고 생각해야 함

# 선형큐1

# 큐로 사용할 빈 리스트
q = []

# 숫자 삽입
for i in range(1,4):
    q.append(i)

print(q)

# 원소 삭제하기
for i in range(3):
    print(q.pop(0), end=",")
print()

print(f"#1 {q}")

# q의 크기가 커지면 RuntimeError 발생.

