T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 정수의 개수로 N 입력
    arr = list(map(int, input().split()))  # 공백으로 구분되는 정수 N개 입력

    # 지그재그 순회를 통한 정렬 문제
    # 가장 큰 수, 가장 작은 수, 다음으로 큰 수, 다음으로 작은 수 .. 순 정렬
#
#     for i in range(N):
#         min_idx = i  # i번째 값을 우선 최소로 정함
#         for j in range(i + 1, N):  # i번째 이후부터 탐색
#             if arr[j] < arr[min_idx]:
#                 min_idx = j  # 최솟값 갱신
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]  # 가장 작은 값 arr[min_idx]와 현재 위치 arr[i] 교환
#
# result = []  # 지그재그 정렬된 값을 담을 리스트
#
# # 바깥 반복문은 최대 N//2 만큼 반복하게 설정 (짝수, 홀수 상관 없이 대응 가능)
# for i in range(N):
#     for j in range(2):  # 큰 값 먼저, 그 다음 작은 값
#         # 첫 번째 반복(j == 0) -> 큰 값: arr[N - 1 - i]
#         # 두 번째 반복(j == 1) -> 작은 값: arr[i]
#
#         # 단, 중복을 피하기 위해 두 인덱스가 같아지는 시점 (i == N - 1 - i)에는 한 번만 추가
#         # 그리고 j == 1일 때는 조건 확인 후 추가해야 함
#
#         # 조건문을 잘 활용해서 중복 없이 result에 append() 하도록 만들기
#
#         print(f"{tc} {result[:10]}")
#
#         left = 0
#         right = N - 1
#         result = []
#
#         while left <= right:
#             result.append(arr[right])
#             if left != right:
#                 result.append(arr[left])
#             left += 1
#             right -= 1

T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 정수의 개수로 N 입력
    arr = list(map(int, input().split()))  # 공백으로 구분되는 정수 N개 입력

    # 지그재그 순회를 통한 정렬 문제
    # 가장 큰 수, 가장 작은 수, 다음으로 큰 수, 다음으로 작은 수 .. 순 정렬

    for i in range(N):
        min_idx = i  # i번째 값을 우선 최소로 정함
        for j in range(i + 1, N):  # i번째 이후부터 탐색
            if arr[j] < arr[min_idx]:
                min_idx = j  # 최솟값 갱신
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # 가장 작은 값 arr[min_idx]와 현재 위치 arr[i] 교환

        # 정렬된 값에서 인덱스 위치 기준으로 왼쪽 오른쪽 번갈아 가며 담기
    left = 0
    right = N - 1
    result = []

    while left <= right:
        result.append(arr[right])
        right -= 1

        if left != right:
            result.append(arr[left])
            left += 1

    print(f"#{tc}", *result[:10])