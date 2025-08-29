# 📌 자료구조 정리

## 🟦 큐 (Queue)

### 개념
- 선입선출(FIFO, First In First Out) 구조
- 먼저 들어온 데이터가 먼저 나감
- 줄 서기와 같은 원리

### 적용 사례
- BFS(너비 우선 탐색)
- 운영체제 스케줄러 (프로세스 대기열)
- 프린터 출력 대기열

### 문제 풀이 방식
```python
from collections import deque

def bfs(start):
    visited = [0] * (N+1)
    q = deque([start])
    visited[start] = 1

    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = visited[now] + 1
                q.append(nxt)
```

## 🟩 스택 (Stack)

### 개념
- 후입선출(LIFO, Last In First Out) 구조
- 나중에 들어온 데이터가 먼저 나감
- 접시를 쌓고 꺼내는 원리와 같음

### 적용 사례
- DFS(깊이 우선 탐색)
- 수식 계산 (후위 표기법, 괄호 검사)
- 함수 호출 (Call Stack), 실행 취소(Undo)

### 문제 풀이 방식
```python
def dfs(start):
    stack = [start]
    visited = [0] * (N+1)

    while stack:
        now = stack.pop()
        if not visited[now]:
            visited[now] = 1
            for nxt in graph[now]:
                if not visited[nxt]:
                    stack.append(nxt)
```


---

## 🟨 트리 (Tree)

### 개념
- 루트(root)에서 시작해 가지처럼 뻗어나가는 계층 구조
- 주요 용어:
  - 루트(root), 부모(parent), 자식(child), 리프(leaf), 높이(height)
- 이진 트리(Binary Tree): 자식 노드가 최대 2개
- 특수한 트리:
  - 이진 탐색 트리(BST): 왼쪽 < 부모 < 오른쪽
  - 힙(Heap): 부모 ≤ 자식(최소 힙), 부모 ≥ 자식(최대 힙)

### 적용 사례
- 이진 탐색 트리: 빠른 검색과 정렬 (O(logN))
- 힙: 우선순위 큐 구현
- 디렉토리 구조, 조직도, 파서(Parser)

### 문제 풀이 방식
```python
def pre_order(n):
    if n:
        print(n)              # 부모
        pre_order(left[n])    # 왼쪽
        pre_order(right[n])   # 오른쪽

def in_order(n):
    if n:
        in_order(left[n])
        print(n)              # 부모
        in_order(right[n])

def post_order(n):
    if n:
        post_order(left[n])
        post_order(right[n])
        print(n)              # 부모
```

---

# ✅ 종합 비교

| 자료구조 | 개념 | 주요 활용 | 문제 풀이 키포인트 |
|----------|------|-----------|-------------------|
| 큐 | FIFO (선입선출) | BFS, 대기열 | `append`, `popleft`로 레벨 탐색 |
| 스택 | LIFO (후입선출) | DFS, 수식 계산 | `append`, `pop`으로 깊이 탐색 |
| 트리 | 계층 구조 | BST, 힙, 디렉토리 | 순회(전위·중위·후위), 힙 삽입/삭제 |

# 📌 그래프 탐색

## 🟦 BFS (Breadth-First Search)

### 개념
- 너비 우선 탐색
- 시작점에서 가까운 노드부터 차례대로 방문
- **큐(Queue)** 자료구조를 사용 (FIFO)

### 적용 사례
- 최단 거리 탐색 (미로, 그래프 경로 길이)
- 네트워크 전파, 레벨 탐색
- 퍼즐/게임 최단 이동 횟수 문제

### 문제 풀이 방식
```python
from collections import deque

def bfs(start):
    visited = [0] * (N+1)
    q = deque([start])
    visited[start] = 1

    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = visited[now] + 1
                q.append(nxt)
```

---

## 🟩 DFS (Depth-First Search)

### 개념
- 깊이 우선 탐색
- 한 경로를 끝까지 탐색한 뒤, 다른 경로로 돌아와 탐색
- **스택(Stack)** 또는 **재귀(Recursion)** 활용

### 적용 사례
- 그래프 연결 요소 찾기
- 백트래킹 (퍼즐, 경우의 수 탐색)
- 위상 정렬, 경로 탐색

### 문제 풀이 방식

```python
def dfs(start):
    stack = [start]
    visited = [0] * (N+1)

    while stack:
        now = stack.pop()
        if not visited[now]:
            visited[now] = 1
            for nxt in graph[now]:
                if not visited[nxt]:
                    stack.append(nxt)
```

---

# ✅ BFS vs DFS 비교

| 탐색 방식 | 원리 | 자료구조 | 대표 활용 |
|-----------|------|-----------|-----------|
| BFS | 가까운 노드부터 탐색 | 큐(FIFO) | 최단 거리, 레벨 탐색 |
| DFS | 깊은 경로부터 탐색 | 스택(LIFO), 재귀 | 백트래킹, 모든 경우 탐색 |
