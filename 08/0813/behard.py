T = 10  # 테스트케이스는 10개로 고정

# 가로 방향 회문 판별
def is_pal_row(board, r, start, length):
    left = start                      # 왼쪽 포인터 시작
    right = start + length - 1        # 오른쪽 포인터 시작
    # length//2 쌍만 비교하면 되므로, 포인터가 서로 다른 칸을 가리키는 동안만 비교
    while left < right:
        if board[r][left] != board[r][right]:  # 양끝 문자가 다르면
            return False               # 회문이 아님
        left += 1                      # 왼쪽 포인터 오른쪽 이동
        right -= 1                     # 오른쪽 포인터 왼쪽 이동
    return True                        # 끝까지 다 같으면 회문

# 세로 방향 회문 판별
def is_pal_col(board, c, start, length):
    top = start                        # 위쪽 포인터 시작
    bottom = start + length - 1        # 아래쪽 포인터 시작
    # length//2 쌍만 비교: 서로 다른 칸일 때만 비교
    while top < bottom:
        if board[top][c] != board[bottom][c]:  # 위/아래 문자가 다르면
            return False                # 회문이 아님
        top += 1                        # 위쪽 포인터 아래로 이동
        bottom -= 1                     # 아래쪽 포인터 위로 이동
    return True                         # 끝까지 다 같으면 회문

for _ in range(1, T + 1):
    tc = int(input())                      # 입력에서 실제 케이스 번호 읽기
    board = [input() for _ in range(100)]  # 100줄 글자판 저장
    answer = 1                              # 최소 회문 길이(초기값)

    # 길이 100부터 1까지 줄여가며 검사 (최장부터 확인)
    for length in range(100, 0, -1):
        found = False                       # 해당 길이에서 회문을 찾았는지 여부
        end = 100 - length + 1              # 시작 위치의 최댓값 + 1 (범위 상한)

        # 행/열 검사: i는 행 또는 열 인덱스로 사용
        for i in range(100):                # 행/열 고정
            for start in range(end):        # 시작 위치만 이동
                # 가로 또는 세로 중 하나라도 회문이면
                if is_pal_row(board, i, start, length) or is_pal_col(board, i, start, length):
                    answer = length         # 최장 길이 갱신
                    found = True
                    break                   # 시작점 탐색 종료
            if found:
                break                       # 행/열 루프 종료
        if found:
            break                           # 길이 루프 종료(최장 확정)

    print(f"#{tc} {answer}")                # #부호 + 테스트케이스 번호 + 공백 + 최장 회문 길이

