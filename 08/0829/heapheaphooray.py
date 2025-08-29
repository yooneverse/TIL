# 최대 힙으로 사용할 배열
heap = [0] * 11

# 마지막으로 넣은 원소의 위치를 기억
last = 0

# 삽입
def enq(item):
    global last
    # item 을 맨 마지막 자리에 추가
    # 맨 마지막 위치 : last +1
    last += 1
    heap[last] = item

    # 일단 넣어봤는데 여기가 니 자리가 맞아??
    # 최대힙 : 부모 > 자식
    # item의 크기와 부모 노드의 크기를 비교해서 교환
    child = last
    # 완전이진트리이므로 부모 = 자식 / 2 _ 정수가 나와야 하니까 //2
    parent = child // 2

    # child에 있는 값과 parent에 있는 값을 비교
    # 부모 노드가 존재하고, 부모 노드보다 자식 노드가 크면
    # 자리를 '계속' 교환해라
    while parent != 0 and heap[parent] < heap[child]:
        heap[child], heap[parent] = heap[parent], heap[child]

        # 한 칸씩 위로 당기는 과정, 부모가 다시 또다른 자식이 되고 부모 찾아가기
        child = parent
        parent = child //2

lst = [6,5,4,1,4,2,9,8,10,7]

for i in range(10):
    enq(lst[i])

print(heap)

# 삭제

def deq():
    global last
    # 루트 노드 삭제 전에 기억
    root = heap[1]

    # 마지막 위치에 있는 원소를 루트 자리로 땡겨온다
    heap[1] = heap[last]

    # 원소 제거 했으니 위치도 하나 줄어들어요
    last -= 1

    # 일단 루트자리에 마지막 원소 데려왔는데
    # 거기가 니 자리 맞아??

    # 부모 > 자식

    # 완전이진트리에서 부모와 지식의 인덱스
    p = 1
    c = p * 2 # 완전 이진 트리니까 왼쪽은 무조건 있음

    # 자식이 두 명이면 그 중에 큰 자식과 비교해서
    # 부모와 자리 교환
    while c <= last:

        # c + 1은 오른쪽 자식 번호인데
        # 이 오른쪽 자식이 존재하는가
        # 존재함과 동시에 오른쪽 자식이 왼쪽보다 큰가
        if c + 1 <= last and heap[c] < heap[c+1]:
            # 그러면 비교 대상이 되는 자식은 오른쪽
            c = c + 1

        # 자식이 부모보다 큰지 확인하고 교환
        if heap[p] < heap[c]:
            heap[p], heap[c] = heap[c], haep[p]
            p = c       # 자식이 새로운 부모가 되고
            c = c * 2   # 새로운 부모를 기준으로 왼쪽 자식이 됨

        else:
            # 부모가 자식보다 크면 맞는 자리이고 자리 바꾸기 중단하면 됨
            break

    # 처음에 기억해놨던 삭제 루트 return
    return root

lst = [6,5,4,1,4,2,9,8,10,7]

for i in range(10):
    enq(lst[i])
    
    print(heap)

for i in range(10):
    print(deq(), end=" , ")