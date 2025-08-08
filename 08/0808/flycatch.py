T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_fly = 0  # 최대로 잡은 파리 수 초기화


    for i in range(N - M + 1):  # 파리채 휘두를 행
        for j in range(N - M + 1):  # 파리채 휘두를 열
            total = 0  # 잡은 수 초기화

            for p in range(i, i + m):
                for q in range(j, j+m):
                    total += matrix[p][q]  # 잡은 파리 총 합(sum 함수 없이 구해야 함) m*m 배열이니까 범위는 [p][j:j+m]

            if max_fly < total:  # 잡은 수가 최댓값보다 크면
                max_fly = total  # 최댓값 교환 이루어짐

    # 각 영역의 파리 갯수는 30 이하

    # 출력 값
    print(f"#{tc} {max_fly}")

            # 잡은 파리 총 합(sum 함수 없이 구해야 함) m*m 배열이니까 범위는 [p][j:j+m]
