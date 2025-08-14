T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())

    # 간선 정보는 이어서 한 줄에 2*E개가 들어온다고 가정
    graph = list(map(int, input().split()))

    # V+1 x V+1 크기로 생성 (1-indexed)
    adjM = [[0] * (V + 1) for _ in range(V + 1)]

    # 간선 정보 입력 (유향 그래프 기준; 무향이면 adjM[g][s] = 1도 추가)
    for i in range(E):
        s, e = map(int, input().split())

        adjM[s][e] = 1

    S,G = map(int, input().split())

    # S에서 G로 갈 수 있는가?
    # 탐색 중에 G 만나면 가능하다고 고치고, 일단 못 가는 상황 가정
    answer = 0

    visited = [0] * (V + 1)

    # X 번 탐색한 적 있다. => visited[x] = 1
    # y 번 탐색한 적 없다. => visited[y] = 0

    # DFS (반복문+스택) 로 정점 탐색
    def DFS(s, V):

        stack = []  # 되돌아올 정점 저장용 스택
        v = s  # 현재 정점
        visited[s] = 1  # 시작점 방문 체크

        while True:

            # 현재 위치가 도착지점 G인가?
            if v == G:
                # S에서 G로 가는 길 발견
                answer = 1
                break


            # v에서 갈 수 있는 정점 찾기
            for nv in range(1, V + 1):
                # nv 정점이 v와 인접하고, 이전에 방문한 적 없어야 함
                if adjM[v][nv] == 1 and visited[nv] == 0:
                    stack.append(v)  # 되돌아올 곳 저장
                    # nv는 방문했다고 표시
                    visited[nv] = 1
                    # 현재 위치 변경해서 이동
                    v = nv
                    # 이동하면 다른 정점은 안 봄
                    break
            else:
                # 더 갈 곳이 없으면 되돌아감
                if stack:
                    v = stack.pop()
                else:
                    break

    print(f"#{tc} {answer}")
