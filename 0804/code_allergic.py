
# #답을 나타낼 변수를 만들고, 예외 경우가 주어질 경우 그 값으로 초기화를 해놓으면 좋음
# #만족하지 못하면 초기화 된 값으로 가게 하면 되기 때문

# T = int(input())
# for tc in range(1,T+1):
#     # tc는 테스트 케이스 번호, 1부터 시작
#     N = int(input())




# # 5x5 배열 입력 받기
# arr = [list(map(int, input().split())) for _ in range(N)]

# # 델타: 중심 (2,2) 기준으로 5개 지점 방문 (우하향 대각선)
# di = [-2, -1, 0, -1, -2]
# dj = [-2, -1, 0, 1, 2]

# # 중심 좌표
# i, j = 2, 2

# # 델타 탐색
# for d in range(5):
#     ni = i + di[d]
#     nj = j + dj[d]


#
# # 정사각형
#
# T = 10
# for tc in range(1, T + 1):
#     N = 100
#
# matrix = [list(map(int, input().split())) for _ in range(N)]
#
# max_sum = 0
#
# # 행의 합
# for i in range(N):
#     row_sum = 0
#     for j in range(N):
#         row_sum += matrix[i][j]
#     if row_sum > max_sum:
#         max_sum = row_sum
#
#
# #열의 합
# for j in range(N):
#     col_sum = 0
#     for i in range(N):
#         col_sum += matrix[j][i]
#     if col_sum > max_sum:
#         max_sum = col_sum

# arr = [3,6,7,1,5,4]
#
# n = len(arr)    # n : 원소의 개수
#
# for i in range(1<<n) : # 1<<n : 부분집합의 개수
#    for j in range(n) : # 원소의 수만큼 비트 비교
#        if i & (1<<j) : # i의 j번 비트가 1인 경우
#            print(arr[j], end=",") #j번 원소 출력
#    print(f' : {i:06b}')
# print()

T = int(input())  # 테스트 케이스 수

for test_case in range(1, T + 1):
    N, K = map(int, input().split())  # 격자 크기 N, 단어 길이 K
    grid = [[0] * N for _ in range(N)]  # 격자를 0으로 초기화

    # 색칠 정보를 입력받아 격자에 반영
    for _ in range(K):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                if color == 1:  # 검정이면 단어가 못 들어가게 표시
                    grid[i][j] += 1

                    #하양 칸은 0이므로 생략되나, 단어가 들어갈 수 있는 칸은 0인 칸임을 알아야 함

    total = 0  # 단어가 들어갈 수 있는 자리 수

    # 가로 방향 확인
    for i in range(N):  # 행을 하나씩 봄
        count = 0  # 연속된 0의 개수
        for j in range(N):
            if grid[i][j] == 0:
                count += 1  # 단어가 들어갈 수 있는 칸
            else:
                if count == K:
                    total += 1  # 정확히 K칸이면 하나 추가
                count = 0  # 벽을 만나면 리셋
        # 줄이 끝났고, 벽을 만나지 않은 경우 count가 안 되니까 마지막으로 다시 검토
        if count == K:
            total += 1

    # 세로 방향 확인
    for j in range(N):  # 열을 하나씩 봄
        count = 0
        for i in range(N):
            if grid[i][j] == 0:
                count += 1
            else:
                if count == K:
                    total += 1
                count = 0
        if count == K:
            total += 1

    # 결과 출력
    print(f"#{test_case} {total}")
