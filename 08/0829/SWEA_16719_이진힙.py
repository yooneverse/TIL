import heapq

T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 원소 개수
    nums = list(map(int, input().split())) # 서로 다른 자연수 한 줄 리스트로 받아오기

    heap = []
    for num in nums:
        heapq.heappush(heap, num)     # 부모 노드 < 자식 노드, heapq 쓰니까 자동으로 최소 힙 됨

    # 문제 힌트가 조상을 인덱스로 제시하고 있으니까
    # 마지막 노드 인덱스로 구하기
    # 자식 중 맨 마지막 자식이니까 child로
    child = len(heap) - 1
    # 조상 노드들의 합_부모들의 합
    parent_sum = 0

    # 부모 인덱스를 따라 올라가며 값 합산
    # 맨 위 루트 노드가 아닐 때까지, 즉 0이 아닐 때까지 올라감
    while child > 0:
        child = (child - 1) // 2       #자식이 부모가 되고 부모가 다시 자식이 됨
        parent_sum += heap[child]

    print(f"#{tc} {parent_sum}")

# heapq 없이

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    heap = [0] * (N + 1)
    last = 0

    def enq(child):
        global last
        last += 1
        heap[last] = child

        child = last
        parent = child // 2

        parent_sum = 0

        while parent != 0 and heap[parent] > heap[child]:
            heap[child], heap[parent] = heap[parent], heap[child]

            # 부모를 따라 올라가며 값 합산하기 위해서
            # 위로 올라가기
            child = parent
            parent = child // 2

        for num in nums:
            enq(num)

        parent_sum=0
        node = last // 2
        while node > 0 :
            parent_sum += heap[node]
            node // 2

        print(f"#{tc} {parent_sum}")










