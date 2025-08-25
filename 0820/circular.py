N = 10

#원형큐 초기화
CQ = [0] * 10
front=rear=0
# 원형큐는 front를 위한 자리 1개를 비워둔다
# 비워 두는 자리는 고정이 아님

def is_full():
    return (rear+1) % N == front

for i in range(1,11):
    if not is_full():
        rear = (rear +1) % N
        CQ[rear] = i

print(CQ, front, rear)

for i in range(9):
    front = (front+1) % N
    print(CQ[front], end = ",")
print()

# front 위해 비워둔 자리는 삭제할 때마다 바뀜
print(CQ, front, rear)


from collections import deque
dq = deque()
dq.append(1)
print(dq.popleft())
print(dq)