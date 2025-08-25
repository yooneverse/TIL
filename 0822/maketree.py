"""
부모 노드 번호를 인덱스로 사용해서 자식 노드 번호를 저장하는 법
4
1 2 1 3 3 4 3 5
"""

# 첫번째 줄 : 간선의 개수 (E)
E = int(input())
N = 5
# 트리 노드 정보 한줄로 입력
tree = list(map(int, input().split()))

# left_child[i] => i번 노드의 왼쪽 자식 노드 번호
left_child = [0] * (N + 1)
# right_child[i] => i번 노드의 오른쪽 자식 노드 번호
right_child = [0] * (N + 1)

for i in range(4):
    p = tree[i*2] # 부모 노드
    c = tree[i*2+1] # 자식 노드

    #p번 노드의 왼쪽 자식이 없으면 c를 p의 왼쪽 자식으로
    if left_child[p] == 0:
        left_child[p] = c

    else:
        right_child[p] = c

print("부모 번호:" , *list(range(N+1)))
print("==================")
print("왼쪽 자식" *left_child)
print("오른쪽 자식" *right_child)


