'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
# V : 정점의 개수
# E : 간선의 개수
V , E = map(int, input().split())

#정점들의 연결 정보가 입력으로 들어온다.
graph = list(map(int, input().split()))

# 인접행렬
# 어떤 정점 x와 어떤 정점 y가 연결되어 있는지 여부를 True(1) or False(0)으로 나타냄
# True(1) ==> 연결되어 있다. x에서 y로 가는 간선이 존재 adjM[x][y] = True // adjM[x][y] = 1
# False(0) ==> 연결 안 되어 있다. x에서 y로 가는 간선이 없음 adjM[x][y] = False // adjM[x][y] = 0
adjM = [[0] * (V+1) for _ in range(V)]

# i : 간선 번호
for i in range(E):
    # s 정점과 e 정점은 연결되어 있다 (인접해있다)
    s, e = graph[i*2], graph[i*2+1]

    # s 정점에서 e 정점으로 가는 간선이 있음 표시
    adjM[s][e] = 1
    # 무향 그래프의 경우에만, e 정점에서 s 정점으로 가는 간선이 있음 표시
    adjM[e][s] = 1

    # print(adjM[i])

def DFS(s, N):
    visited = [0] * (N+1)
    # X 번 탐색한 적 있다. => visited[x] = 1
    # y 번 탐색한 적 없다. => visited[y] = 0

    # 가장 마지막에 방문한 정점으로 쉽게 돌아가기 위해 스택 사용
    stack = []

    # 현재 탐색중인 정점 번호
    v = s

    # 시작 정점 방문했다고 체크 : 1로 바꾼다
    visited[s] = 1
    print(v, end=" ")

    while True:
        # 현재 정점 v에서 탐색
        # v에서 갈 수 있는 다른 정점 찾기
        # nv: 다른 정점 번호
        for nv in range(1,V+1):
            # 갈 수 있다 => v에서 nv로 갈 수 있느냐를 판단
            # v와 nv가 인접해 있고, nv를 이전에 방문한 적이 없다면 갈 수 있음
            # if adjM[v][nv] and not visited[nv]:
            if (adjM[v][nv]) and (visited[nv] == 0):
                # v에서 nv로 가는 길이 있고, nv를 방문한 적도 없음
                # nv로 일단 가자
                # 가기 전에 현재 위치를 스택에 저장(왔던 길 기억)
                stack.append(v)
                # nv로 이동
                v = nv
                # nv에 다음에 또 오면 안되니까 방문했다고 표시
                visited[nv] = 1
                print(nv, end = " ")

                # nv로 이동했으니 다른 갈 수있는 정점은 보지 않아도 됨

                break

        #for-else
        else:
            # 중간에 break한 적이 없다면 실행
            # 갈 수 있는 다른 이 정점을 찾지 못했음(현재위치 v  기준)
            # 갈 곳이 없으니 돌아감. 돌아갈 곳은 스택에 저장되어있음
            # 가장 최근에 방문했던 곳으로 돌아가야 하는데, 스택은 후입선출 구조라서
            # 원소를 하나 꺼내면 그곳이 바로 최근에 방문했던 정점이 됨
            # 꺼내기 전에 비어있지 않은가 확인
            if stack:
                # 비어있지 않으면 돌아갈 곳이 잇음
                v = stack.pop()
            else:
                # 더이상 갈 수 있는 곳도 없고 돌아갈 곳도 없으면 탐색종료
                break

        DFS(1,V)
