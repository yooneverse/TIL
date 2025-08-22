'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
13
2 1 2 3 1 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''


# 트리 노드의 수
N = int(input())
# 트리 정보 => 두 개씩 끊어서 읽으면 앞이 부모번호, 뒤가 자식번호
tree = list(map(int, input().split()))

# 부모 노드 번호를 인덱스로 사용하는 방법
cleft = [0] * (N+1)
cright = [0] * (N+1)

for i in range(N-1):
    # 앞이 부모
    p = tree[i*2]
    # 뒤가 자식
    c = tree[i*2+1]

    # p번 노드의 왼쪽 자식이 없다면
    if cleft[p] == 0:
        # c번 노드를 p번 노드의 왼쪽 자식으로
        cleft[p] = c
    else:
        #왼쪽 자식 있으면
        cright[p] = c

print(cleft)
print(cright)

# 서브트리로 쪼개고 나서
# 루트 : V
# 왼쪽 SUB : L
# 오른쪽 SUB : R

# 1. 전위 순회 : V - L - R
def preorder(t):
    # t번 노드가 존재하는 노드면 순회
    if t:
        # V 노드에서 해야 할 연산 코드 작성
        print(t, end=" ")
        preorder(cleft[t])
        preorder(cright[t])

preorder(1)
print()

# 2. 중위 순회 : L V R
def inorder(t):
    if t:
        inorder(cleft[t])
        print(t, end= " ")
        inorder(cright[t])

inorder(1)
print()

# 3. 후위 순회 : L R V
def postorder(t):
    if t:
        postorder(cleft[t])
        postorder(cright[t])
        print(t, end=" ")

postorder(1)
print()

