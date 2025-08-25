# T = int(input())
# for ts in range(1, T + 1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#
#     max_idx = 0
#     min_idx = 0
#
#     for i in range(1, N):
#         if arr[i] >= arr[max_idx]:
#             max_idx = i
#         if arr[i] < arr[min_idx]:
#             min_idx = i
#
#     print(abs(max_idx - min_idx))

# N=2a x 3b x 5c x 7d x 11e
# N이 주어질 때, a,b,c,d,e 출력하라
# N = 2 이상 10,000,000 이하

T = int(input())
for tc in range(1, T+1):
    N = int(input())

