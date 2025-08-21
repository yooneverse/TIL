from collections import deque

"""
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""

# s : 탐색을 시작하는 정점 번호
def bfs1(s):
    # 방문 배열 (중복 방문 체크 + 거리 계산 가능)
    visited = [0] * (V+1)

    # 큐 (다음에 방문할 곳 예약)
    q = deque()

    # 시작 정점을 큐에 넣고 탐색 시작
    q.append(s)
    visited[s] = 1

    # 큐 안에 방문할 곳이 남아있다면 탐색 계속
    while q:
        # 큐에서 다음 방문할 곳 하나 꺼내오기
        v = q.popleft()
        print(v, end=" ")

        # v와 인접한 정점 탐색
        for nv in range(1, V+1):
            # 1. v에서 nv번 정점으로 갈 수 있다 (adj_m[v][nv] == 1)
            # 2. 아직 방문하지 않았다 (visited[nv] == 0)
            if adj_m[v][nv] == 1 and not visited[nv]:
                # nv는 방문 예정임을 큐에 저장
                q.append(nv)
                # nv 방문 체크 (거리 = v까지 거리 + 1)
                visited[nv] = visited[v] + 1

    # 리스트 부분은 강사님 코드 보고 다시 배우기


# 정점의 개수 : V
# 간선의 개수 : E
V, E = map(int, input().split())

# 인접 행렬
adj_m = [[0] * (V+1) for _ in range(V+1)]
# 인접 리스트
adj_l = [[] for _ in range(V+1)]

# 그래프 정보가 한 줄로 들어옴
graph = list(map(int, input().split()))

for i in range(E):
    s, e = graph[i*2], graph[i*2+1]

    # 인접 행렬
    adj_m[s][e] = 1
    adj_m[e][s] = 1

    # 인접 리스트
    adj_l[s].append(e)
    adj_l[e].append(s)

# BFS 탐색 실행
bfs1(1)




