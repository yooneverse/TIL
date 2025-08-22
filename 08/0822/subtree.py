T = int(input())

for tc in range(1, T+1):
    # 간선 개수 E, 확인할 노드 번호 N  띄어쓰기로 들어옴
    E, N = map(int, input().split())
    # 부모-자식 관계 노드 쌍 입력
    tree = list(map(int, input().split()))

    # 자식 정보 저장
    children = [[] for _ in range(E+2)]  # 간선 기준 최대 E+1개니까 안정적으로 E+2, 문제에서 2차원 배열로 제시
    for i in range(E):
        p = tree[2*i]      # 부모
        c = tree[2*i + 1]  # 자식
        children[p].append(c) # 부모 p의 자식 자리에 c를 추가

    # 서브트리 내 노드 탐색 함수
    def sub_cnt(node):
        cnt = 1  # 자기 자신 포함
        for child in children[node]: # 자식 노드 안 숫자 합 구하기
            cnt += sub_cnt(child)
        return cnt


    # 출력할 것 : 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수
    sub_cnt(N)
    print(f"#{tc} {sub_cnt(N)}")


T = int(input())

for tc in range(1, T+1):
    # 간선 개수 E, 확인할 노드 번호 N  띄어쓰기로 들어옴
    E, N = map(int, input().split())
    # 부모-자식 관계 노드 쌍 입력
    tree = list(map(int, input().split()))

    # 자식 정보 저장
    cleft = [0] * (E + 2)
    cright = [0] * (E + 2)

    for i in range(E):
        p = tree[2*i]        # 부모
        c = tree[2*i + 1]   # 자식
        if cleft[p] == 0:    # 왼쪽에 아직 없으면
            cleft[p] = c      # 왼쪽 자식으로
        else:                  # 왼쪽이 있으면
            cright[p] = c    # 오른쪽 자식으로

    # 순회하며 노드 수 세기
    def preorder(t):
        if t != 0:
            sub_cnt = 1 # 자기 자신 포함
            sub_cnt += preorder(cleft[t]) # 왼쪽 자식 값 더하기
            sub_cnt += preorder(cright[t]) # 오른쪽 자식 값 더하기
            return sub_cnt
        return 0

    result = preorder(N)
    print(f"#{tc} {result}")










