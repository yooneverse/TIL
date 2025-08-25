from collections import deque

# 2차원 배열에서는 인접한 정점 => 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

N = 7
maze = [0,0,0,0,0,0,0]

# 강사님 코드에서 데려오면 됨

# si,sj : 시작 위치 좌표(si: 행번호, sj: 열번호)
def bfs(si,sj):
    # 방문체크(중복체크) 배열
    visited = [[0] * N for _ in range(N)]
    # 큐 생성
    q = deque()
    # 시작 위치 큐에 넣고
    # 시작 위치 : 행번호, 열번호
    q.append((si,sj))

    # 큐 안에 탐색할 좌표가 남아있으면 계속
    while q:
    # 큐에서 다음 탐색 위치 꺼내오기
        i, j = q.popleft()

    # 이 꺼낸 위치(내가 방문하고 있는 위치) 도착점인지 판단
    if maze[i][j] == 99:
        print(f"탈출: ({i}{j}), 거리: {visited[ni][nj]}")

    # 이 i,j와 인접한 상하좌우 방향 확인
    # 상하좌우에 방문할 곳이 있는지 판단
    for d in range(4):
        # 상하좌우로 1칸씩 이동한 좌표 계산
        ni = i + di[d]
        nj = j + dj[d]

        # 이동 후 좌표가 ni, nj 방문 가능한 위치인가?
        # 1. ni, nj가 유효한 인덱스 범위 안에 좌표가 있는지
        # 2. 방문한 적 없어야 함
        # 3. maze[ni][nj] != 1: 벽(1)이 아니어야 이동 가능
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and maze[ni][nj] != 1:
            pass
        # is_valid는 나중에 적용

            # 위의 3개 조건을 만족하면 ni,nj는 방문 가능
            # 큐에 다음에 방문할 것임을 예약
            q.append((ni,nj))
            # 중복방지 + 거리계산
            visited[ni][nj] = visited[i][j] + 1

    # while 문 종료 후 코드가 여기까지 실행됨
    # 중간에 우리가 찾는 목표 지점 찾지 못함
    print("실패")
    return -1