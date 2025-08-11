T = int(input())


#tc=test_case 불러오기
for tc in range(1, T+1):
    input()
    # 지도 별로 첫 줄에 N과 M이 공백으로 구분되어 주어짐
    N,M = map(int, input().split())

    # 각 칸에는 각 구역 높이가 0이상 20 이하의 정수로 표시
    # 가장 자리는 인접 구역 정보가 부족하므로 안전구역에서 제외

    # N*M 배열의 지도 만들기
    safe_map = [list(map(int, input().split())) * N for _ in range(M)]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    for i in range(N):
        for j in range(M):
            safe = 0 # 안전구역 수
            near = 0 # 인접구역

            for r in range(i, i+M):
                for c in range(j, j+M):
                    safe = safe_map[i][j]

                #인접구역 탐색(상하좌우)
                for p in range(4): # 인덱스 0~3: 상하좌우
                    for k in range(N-1): #높이 탐색
                        ni = i + di[i] * k
                        nj = i + dj[j] * k
                        if 0 <= ni < N and 0 <= nj <= M:
                            near += safe_map[ni][nj] #인접구역

                            if near < safe: # 인접구역보다 높으면 안전구역이 됨
                                safe += 1 #안전구역 수 합산

# 출력 형식 = #(지도번호) (안전구역 수)
print(f"{map} {safe}")
