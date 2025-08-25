# T = int(input())  # 테스트케이스 개수
#
# for test_case in range(1, T + 1):
#     N, M = map(int, input().split())  # N: 수열의 길이, M: 구간 길이
#     arr_v = list(map(int, input().split()))  # N개의 정수 입력받기
#
#     # 초기 구간합 계산 (앞에서 M개 더함)
#     current_sum = 0
#     for i in range(M):
#         current_sum += arr_v[i]
#
#     max_sum = current_sum
#     min_sum = current_sum
#
#     # 구간을 하나씩 오른쪽으로 이동하며 합 갱신
#     for i in range(M, N):
#         prev_v = arr_v[i - M]  # 빠지는 값
#         now_v = arr_v[i]       # 새로 추가되는 값
#
#         current_sum = current_sum - prev_v + now_v  # 구간합 갱신
#
#         # 최댓값과 최솟값 갱신
#         if current_sum > max_sum:
#             max_sum = current_sum
#
#         if current_sum < min_sum:
#             min_sum = current_sum
#
#     # 결과 출력 (각 테스트케이스마다 한 번)
#     print(f"#{test_case} {max_sum - min_sum}")

T = int(input())

COUNT = [0] * (T + 1)

for test_case in range(T):
    num = input()  # 한 줄씩 입력 받기
    COUNT[num%10] += 1
    num //= 10

print("모든 자리수 빈도:", COUNT)
