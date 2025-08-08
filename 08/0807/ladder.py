T = int(input())

for tc in range(1, T + 1):
    N = 100  # 사다리 크기 (100*100)
    input()
    ladder = [list(map(int, input().split())) for _ in range(N)]  # 2차원 배열로 사다리 만들기

    # 사다리 선 == 1
    # 도착지점 == 2
    # 평면 == 0

    for j in range(N):
        if ladder[N - 1][j] == 2:  # 도착 지점 찾기 (맨 아래 행에서 2가 있는 열)
            row = N - 1
            col = j

            while row > 0:
                # 좌측에 1이 있으면 왼쪽으로 이동
                # 조건: 한 막대에서 출발한 가로선이 다른 막대를 가로질러 이어지지 않음
                if col > 0 and ladder[row][col - 1] == 1:
                    while col > 0 and ladder[row][col - 1] == 1:
                        col -= 1
                    row -= 1
                # 우측에 1이 있으면 오른쪽으로 이동
                elif col < N - 1 and ladder[row][col + 1] == 1:
                    while col < N - 1 and ladder[row][col + 1] == 1:
                        col += 1
                    row -= 1
                # 양쪽 다 없으면 위로 이동
                else:
                    row -= 1

            print(f"#{tc} {col}")  # 맨 위에 도달했을 때의 열 인덱스가 출발점
            break  # 다음 테스트케이스로 넘어가기

            # 방향 전환 이후엔 다시 아래 방향으로만 이동하게 되며, 바닥에 도착하면 멈추게 됨
            # 거꾸로 올라가니까 방향 전환 이후에 위로 향하며, 맨 위에 닿으면 멈추게 해야 함
            # for j in range(N):
            #     if 맨 아래 행의 j열이 도착지점 2라면:
            #         위치(row, col) 설정
            #         while 위로 올라가기:
            #             좌우 체크 및 이동
            #         break 에서 순회 멈춤
            #
            # print(출발 지점 col)
