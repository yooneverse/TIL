T=int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_fly = 0 # 최대로 잡은 파리 수 초기화
