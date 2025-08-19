lst = [1,2,3]
N = 3

# 자리 교환 방식
# 0번 인덱스랑 누가 자리를 바꿀래?
# 0번 인덱스랑 누가 자리를 바꿀래?
# ...
# N-1번 인덱스랑 누가 자리를 바꿀래
# N번은 안된다

# idx : idx 번에 있는 원소를 다른 위치와 자리 교환
def make_perm(idx):
    
    # 1. 종료 조건
    if idx == N:
        print(lst)
        return

    # 2. 재귀 호출
    # idx랑 누구랑 자리바꿀래? 정해야 함
    # N개 중에 하나 고르면 됨 => 단, idx 번호와 비교해서 idx 이상인 번호와 자리를 교환
    # 자리 바꾸는 대상 j는 idx보다 앞에 있으면 안됨 => 앞에서 바꾼 자리를 원상복구하는 경우가 생기기 때문
    for j in range(idx, N):
        # idx 번이랑 j번 자리 바꿈
        lst[idx], lst[j] = lst[j], lst[idx]
        # idx 번이랑 누구랑 바꿀지 정하기
        make_perm(idx+1)
        # idx 번이랑 j번이 자리를 바꾼 일을 없던 일로 원상복구
        lst[idx], lst[j] = lst[j], lst[idx]

# 0번부터 자리 바꾸기 시작
make_perm(0)