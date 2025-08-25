# 가위바위보 게임
# 1은 가위, 2는 바위, 3은 보
가위 = 1
바위 = 2
보 = 3

def winner(left, right):
    if cards[left] == 가위:
        if cards[right] == 바위:
            return right
        elif cards[right] == 보:
            return left
        else:
            return left if left < right else right

    elif cards[left] == 바위:
        if cards[right] == 보:
            return right
        elif cards[right] == 가위:
            return left
        else:
            return left if left < right else right

    elif cards[left] == 보:
        if cards[right] == 가위:
            return right
        elif cards[right] == 바위:
            return left
        else:
            return left if left < right else right

def tournament(i, j):
    if i==j:
        return i
    else:
        left = tournament(i, (i+j)//2)
        right = tournament((i+j)//2+1, j)
        return winner(left, right)


# 실행-입력부
T = int(input())  # 테스트케이스 입력

for tc in range(1, T + 1):
    N = int(input())
    cards = list(map(int,input().split()))
    win = tournament(0, N-1)
    print(f"#{tc} {win+1}")
