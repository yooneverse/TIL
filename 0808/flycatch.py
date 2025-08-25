# T = int(input())

# for test_case in range(1, T + 1):
#     N, M = map(int, input().split())
#     matrix = [list(map(int, input().split())) for _ in range(N)]

#     max_fly = 0  # 최대로 잡은 파리 수 초기화


#     for i in range(N - M + 1):  # 파리채 휘두를 행
#         for j in range(N - M + 1):  # 파리채 휘두를 열
#             total = 0  # 잡은 수 초기화

#             for p in range(i, i + m):
#                 for q in range(j, j+m):
#                     total += matrix[p][q]  # 잡은 파리 총 합(sum 함수 없이 구해야 함) m*m 배열이니까 범위는 [p][j:j+m]

#             if max_fly < total:  # 잡은 수가 최댓값보다 크면
#                 max_fly = total  # 최댓값 교환 이루어짐

#     # 각 영역의 파리 갯수는 30 이하

#     # 출력 값
#     print(f"#{tc} {max_fly}")

#             # 잡은 파리 총 합(sum 함수 없이 구해야 함) m*m 배열이니까 범위는 [p][j:j+m]

#파리퇴치 3
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N,M = map(int, input().split()) #N은 크기, M은 세기
#     matrix = [list(map(int, input().split())) for _ in range(N)] # N*N 배열 만들기
#
#     max_fly = 0
# # 스프레이를 M의 세기로 분사하면 노즐의 중심이 향한 칸부터 각 방향으로 M칸의 파리 잡음
# # 스프레이는 양 대각선 혹은 십자형으로 분사됨
#     for i in range(N) :# 뿌리기 시작하는 좌표 행
#         for j in range(N) : # 뿌리기 시작하는 좌표 열
#             total += matrix[i][j] # 총 잡은 파리 수
#
#             #델타 리스트로 각 방향 설정(상하좌우, 대각선 왼,오)
#         di1 = [-1, 1, 0, 0] #상하좌우
#         dj1 = [0, 0, -1, 1]
#
#         di2 = [-1, -1, 1, 1]
#         dj2 = [-1, 1, -1, 1]
#
#         for d in range(4):
#             for k in range(1, M+1):
#                 ni = i + di1[d]*k
#                 nj = j + dj1[d]*k
#
#         if max_fly < total:
#             max_fly = total
#
#             #출력
#     print(f"#{tc} {max_fly}")

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N은 격자 크기, M은 세기
    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_fly = 0

    # 델타 리스트 설정
    cross_di = [-1, 1, 0, 0]   # 상하좌우
    cross_dj = [0, 0, -1, 1]

    diag_di = [-1, -1, 1, 1]   # 대각선
    diag_dj = [-1, 1, -1, 1]

    for i in range(N):
        for j in range(N):
            total_cross = matrix[i][j]  # 중심 포함
            total_diag = matrix[i][j]   # 중심 포함

            # 십자형 방향
            for d in range(4):
                for k in range(1, M):
                    ni = i + cross_di[d] * k
                    nj = j + cross_dj[d] * k
                    if 0 <= ni < N and 0 <= nj < N:
                        total_cross += matrix[ni][nj]

            # 대각선 방향
            for d in range(4):
                for k in range(1, M):
                    ni = i + diag_di[d] * k
                    nj = j + diag_dj[d] * k
                    if 0 <= ni < N and 0 <= nj < N:
                        total_diag += matrix[ni][nj]

            # 최댓값 갱신
            more = total_cross
            if total_diag > total_cross:
                more = total_diag

            if max_fly < more:
                max_fly = more

    # 출력
    print(f"#{tc} {max_fly}")
