import heapq
# 최소 힙은 존재함

heap = []

lst = [6,5,4,1,3,2,9,8,7,10]

for i in range(10):
    heapq.heappush(heap, lst[i])

for i in range(10):
    print(heapq.heappop(heap), end=" ")
print()

# 최대로 만들기
for i in range(10):
    heapq.heappush(heap, -lst[i])

for i in range(10):
    print(-heapq.heappop(heap), end=" ")
print()