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

# parent[i] => i번 노드의 부모 노드 번호
parent = [0] * (N+1)

for i in range(E):
    p = tree[i+2]
    c = tree[i*2+1]

    parent[c] = p

print("자식 번호:", *list(range(N+1)))
print("==================")
print("부모 번호:", *parent)


