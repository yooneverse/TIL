T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    # 큐 만들기
    q = [0] * n+m #n의 여유를 더 줘서 rear 값 넣을 수 있게 하기
    front = rear = -1

    for i in arr:
        rear += 1
        q[rear] = i  # arr의 원소 다 큐에 넣기

    for j in range(m):  # m번 반복해서 dequeue, enqueue 진행
        front += 1
        x = q[front]  # dequeue

        rear += 1
        q[rear] = x  #enqueue

    print(f'#{tc} {q[front + 1]}')  # 한번 더 꺼낸 값 출력

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    q = list(map(int, input().split()))  # 숫자 다 큐에 넣기

    # m번 순회 (맨 앞 꺼내서 뒤로 보내기)
    for i in range(m):
        front = q.pop(0)  # 맨 앞 꺼내기
        q.append(front)  # 맨 뒤에 붙이기

    # m번 순회 후 맨 앞 원소 출력
    print(f"#{tc} {q[0]}")
