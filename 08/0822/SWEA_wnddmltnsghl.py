T = 10  # 주어진 테스트 케이스 수(고정)

def in_order(n):
    if n <= N:
        global value
        in_order(n * 2)  # 왼쪽 자식 방문, 갱신된 value 받기
        tree[n] = value  # 현재 노드 값 저장
        value += 1
        in_order(n * 2 + 1)  # 오른쪽 자식 방문

# 근데 정점 정보가 V, L, R 순으로 들어옴

for tc in range(1, T + 1):
    N = int(input())
    nodes = list(map(input().split()))

    in_order(1)              # 루트부터 중위순회