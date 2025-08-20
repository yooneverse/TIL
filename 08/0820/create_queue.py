front = rear = -1
q = [0] * 10

rear += 1 # enq(1)
q[rear] = 1
rear += 1 # enq(2)
q[rear] = 2
rear += 1 # enq(3)
q[rear] = 3

front += 1 # deq()
print(q[front])
front += 1 # deq()
print(q[front])
front += 1 # deq()
print(q[front])

#front가 어디까지 갔느냐가 중요한 것