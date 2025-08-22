
T = int(input()) # 테스트케이스 수

# 구해야 하는 거
# 1. N이 주어졌을 때 완전 이진 트리로 만든 이진 탐색 트리의 루트에 저장된 값
# 2. 동일 상황에서 N/2번 노드(N이 홀수인 경우 소수점 버림)에 저장된 값
# 완전 이진 트리의 노드 번호는 루트를 1번으로 하고 아래로 내려가면서 왼쪽에서 오른쪽 순으로 수가 커짐
# 문제에서 준 사항 : L < V < R

def in_order(n):
    if n <= N:
        global value
        in_order(n * 2)  # 왼쪽 자식 방문, 갱신된 value 받기
        tree[n] = value  # 현재 노드 값 저장
        value += 1
        in_order(n * 2 + 1)  # 오른쪽 자식 방문

for tc in range(1, T+1): # 각 테스트 케이스별로
    N = int(input()) # 노드 개수로 정수 N이 주어짐
    tree = [0] * (N + 1)    # 노드 저장 배열 만들어서 채울 준비
    value = 1               # 채워 넣을 값이고 완전이진트리 번호는 1번부터 시작 => 문제 그림 참고

    in_order(1)              # 루트부터 중위순회

    root_val = tree[1]      # 루트 노드 값
    half_val = tree[N // 2] # N//2번 노드 값(정수니까 //함)


    print(f"#{tc} {root_val} {half_val}")


    def in_order(n, value):
        if n <= N:
            # 왼쪽 자식 방문
            value = in_order(n * 2, value)

            # 현재 노드에 값 저장
            tree[n] = value
            value += 1  # 다음 값 준비

            # 오른쪽 자식 방문
            value = in_order(n * 2 + 1, value)

        # 갱신된 value 반환
        return value

    # 이 부분 다시 정리하기(global 개념 정리 필요)