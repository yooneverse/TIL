T = int(input()) # 테스트케이스(지도) 개수(3<=T<10)

# tc=test_case 불러오기
for tc in range(1, T + 1):
    input()
    N, M, K = input().split()

    # N*N 배열
    # box = [list(input().split()) for _ in range(N)] ** 틀림
    space = [list(input()) for _ in range(N)]
    # 입력받아서 숫자로 못 바꾸니까 리스트로만 문자열 그대로 처리 N줄 입력 받음

    # 문제에서 원하는 답
    # 일단 없다고 가정하고 시작
    row = col = -1


    # 시작점 구하기
    for i in range(N-M+1): #M*M 배열로 찾기
        for j in range(N-M+1):
            # (i, j) 에서부터 M*M 크기 작은 영역을 만들고 별 개수 세기
            star =0
            # 이 작은 영역의 범위를 인덱스로 지정해서 탐색
            # 이 작은 영역의 행번호와 열번호를 ni,nj

            for ni in range(i, i+M):
                for nj in range(j, j+M):  # 중심점에서 M만큼
                    if space[ni][nj] == '*':
                        star += 1

            if star == K:
                # 작은 영역의 별의 개수가 정확히 K개이면
                # 정답 위치 바꾸기
                row = i
                col = j

    # 모든 가능한 (i,j)를 탐색하고 나서 답 출력
    # 자연스럽게 못 찾으면 (-1,-1) 이도록 초기값이 설정되어있어 따로 할 필요 없음
    print(f"{tc} {row} {col}")



