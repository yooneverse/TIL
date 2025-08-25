T = int(input())  # 테스트 케이스 수 입력

for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

def solve_case(N, grid):
    # 1) 각 행 최소값 (하한 계산용)
    row_min_val = [0] * N
    for r in range(N):
        smallest = grid[r][0]
        for c in range(1, N):
            if grid[r][c] < smallest:
                smallest = grid[r][c]
        row_min_val[r] = smallest

    # 2) remain_min_sum[row] = row행부터 끝까지의 최소값 합
    remain_min_sum = [0] * (N + 1)
    for r in range(N - 1, -1, -1):
        remain_min_sum[r] = remain_min_sum[r + 1] + row_min_val[r]

    # 3) 안전한 유한 상한값 (각 행 최대값의 합)
    row_max_sum = sum(max(row) for row in grid)

    used_col = [0] * N
    best = None  # 최소합 후보

    def dfs(row, total):
        nonlocal best

        # 아직 best가 없으면 row_max_sum을 임시 상한으로 사용
        if best is not None:
            curr_upper = best
        else:
            curr_upper = row_max_sum

        # 하한 가지치기
        if total + remain_min_sum[row] >= curr_upper:
            return

        # 모든 행 선택 완료 → 최소합 갱신
        if row == N:
            if best is None or total < best:
                best = total
            return

        # 현재 행에서 열 선택
        for col in range(N):
            if used_col[col]:
                continue

            new_total = total + grid[row][col]
            if best is not None and new_total >= best:
                continue

            used_col[col] = 1
            dfs(row + 1, new_total)
            used_col[col] = 0

    dfs(0, 0)
    return best

# 실행

    answer = solve_case(N, grid)
    print(f"#{tc} {answer}")
