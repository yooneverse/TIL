# 전위순회
def preorder(v):
    if v != 0:                     # 0이면 자식 없음
        print(value[v], end="")
        preorder(left[v])
        preorder(right[v])

# 중위순회
def inorder(v):
    if v != 0:
        inorder(left[v])
        print(value[v], end="")
        inorder(right[v])

# 후위순회
def postorder(v):
    if v != 0:
        postorder(left[v])
        postorder(right[v])
        print(value[v], end="")

N = int(input())  # 노드 개수

value = [""] * (N + 1)
left = [0] * (N + 1)
right = [0] * (N + 1)
nodes = {}      # 문자 → 인덱스
idx = 1         # 1부터 시작 (0은 없음 표시)

for _ in range(N):
    p, l, r = input().split()

    # 부모 등록
    if p not in nodes:
        nodes[p] = idx
        value[idx] = p
        idx += 1
    pi = nodes[p]

    # 왼쪽 자식 등록
    if l != '.':
        if l not in nodes:
            nodes[l] = idx
            value[idx] = l
            idx += 1
        left[pi] = nodes[l]

    # 오른쪽 자식 등록
    if r != '.':
        if r not in nodes:
            nodes[r] = idx
            value[idx] = r
            idx += 1
        right[pi] = nodes[r]

# 루트는 항상 'A'
root = nodes['A']
preorder(root)
print()
inorder(root)
print()
postorder(root)
print()

# 모범답안으로 추정되는 딕셔너리 방법

def preorder(v):
    if v != '.':
        print(v, end="")
        preorder(tree[v][0])
        preorder(tree[v][1])

def inorder(v):
    if v != '.':
        inorder(tree[v][0])
        print(v, end="")
        inorder(tree[v][1])

def postorder(v):
    if v != '.':
        postorder(tree[v][0])
        postorder(tree[v][1])
        print(v, end="")

N = int(input())
tree = {}

for _ in range(N):
    p, l, r = input().split() #v로 안 보고 부모라는 뜻의 p로 할당
    tree[p] = (l, r)

# 항상 'A'부터 시작
preorder('A')
print()
inorder('A')
print()
postorder('A')
print()