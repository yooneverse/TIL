# 안전구역의 조건
# 1. 중간이 상하좌우보다 커야 함
# 2. 상하좌우가 다 있어야 함


T = int(input())

#tc=test_case 불러오기
for tc in range(1, T+1):
    input()
    # 지도 별로 첫 줄에 N과 M이 공백으로 구분되어 주어짐
    N,M = map(int, input().split())

    # 각 칸에는 각 구역 높이가 0이상 20 이하의 정수로 표시
    # 가장 자리는 인접 구역 정보가 부족하므로 안전구역에서 제외

    # N*M 배열의 지도 만들기
    safe_map = [list(map(int, input().split())) for _ in range(N)] # 틀림...기존대로 했어야 했다

    safe_zone = 0

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    # 모든 위치에서 상하좌우 검사
    # 행 번호 i 범위는 0 ~ N-1까지
    # 열 번호 j 범위는 0 ~ M-1까지

    for i in range(N):
        for j in range(M):
            # safe = 0 # 안전구역 수
            # near = 0 # 인접구역

            # (i, j)가 안전 구역인가를 판단
            # 안전하다고 가정하고 검사 시작
            is_safe = True

            # for r in range(i, i+M):
            #     for c in range(j, j+M):
            #         safe = safe_map[i][j]

                #인접구역 탐색(상하좌우)
            for d in range(4): # 인덱스 0~3: 상하좌우
                    ni = i + di[d]
                    nj = i + dj[j]
                    # if 0 <= ni < N and 0 <= nj <= M:
                    #     near += safe_map[ni][nj] #인접구역

                    # (i,j) 안전구역 조건
                    #1. 상하좌우가 모두 (inj)보다 낮아야 함
                    if 0<= ni < N and 0<= nj < M:
                        # 기준위치(i,j)보다 상하좌우 중
                        # 높은 위치(ni,nj) 존재
                        # 이 상황은 (i,j)가 안전구역이 아니게 됨
                        is_safe = False

                    else:
                        is_safe = False

            if is_safe:
                safe_zone += 1

                        # if near < safe: # 인접구역보다 높으면 안전구역이 됨
                        #     safe += 1 #안전구역 수 합산

# 출력 형식 = #(지도번호) (안전구역 수)
print(f"{map} {safe_zone}")
