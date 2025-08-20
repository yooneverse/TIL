# 선형 큐로 푸는 방법
# 백지에서 풀게 연습해보기

T = 10

for _ in range(1, T + 1):  # 테스트 케이스 순회
    n = int(input())  # 테스트 케이스 번호
    arr = list(map(int, input().split()))  # (1) 숫자 8개를 입력 받음

    # 큐 초기화 (넉넉히 잡음)
    q = [0] * 1000000
    front = rear = -1

    # arr 원소를 큐에 넣기
    for i in arr:
        rear += 1
        q[rear] = i

    cycle = 1  # (2) 사이클 만들어서, 사이클 내 숫자만큼 front 값 빼버리기
    while True:
        front += 1
        x = q[front] - cycle

        cycle += 1
        if cycle > 5:
            cycle = 1

        if x <= 0:
            rear += 1  # (3-1) 숫자가 감소할 때, 0보다 작아지는 경우 0으로 유지
            q[rear] = 0
            break  # (3-2) 프로그램 종료

        else:  # 0이 아니면
            rear += 1
            q[rear] = x

    # 출력 (입력받은 번호 그대로)
    print(f"#{n}", *q[rear - 7:rear + 1])


    # 원형 큐로 풀어보기

    T = 10

    N = 8

    CQ = [0] * N
    front = rear = 0

    for i in range(8):
        front = (front + 1) % N
        print(CQ[front], end=",")




