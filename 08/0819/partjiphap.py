lst = [1,2,3,4,5]

N = 5
# 부분집합의 합이 S 이하인 부분집합만 구하라
S = 5 # 한계 정해주기

# 부분집합을 만드는 재귀함수
# make_set(0) : 0번 원소를 부분집합에 넣을지 말지

# make_set(N-1): N-1번 원소를 부분집합에 넣을지 말지..
# make_set(N) : N 번 원소는 없음 => 재귀 호출 중단
# 단계는 원소의 인덱스와 같다고 생각

# idx: 내가 지금 idx번 원소를 부분집합에 넣을지 말지 선택한다는 것
# selected 리스트 : 내가 지금까지 결정한 부분집합에 포함할 원소들의 상태를 나타내는 변수 ≑ visited 변수
# selected[x] == 1 (True) : x번 원소를 부분집합에 넣기로 함
# selected[y] == 0 (False) : y번 원소는 부분집합에 넣지 않기로 함
# s :  idx번 원소까지 부분집합에 넣을지 말지 고민을 할 때, 이 시점까지 완성한 부분집합의 합

def make_set(idx, selected, s):

    # 0. 가지 치기
    # 지금까지 구한 부분집합의 합 s 가
    # 문제에서 원하는 합 S보다 크면 더 진행 xxx (답이 될 확률이 없음)
    if s >S:
        return

    # 1. 종료 조건
    if idx == N:
        # selected 배열을 보고 내가 어떤 원소를 선택했었는지 확인
        subset = []
        for i in range(N):
            if selected[i]:
                subset.append(lst[i])

        print(subset)
        return

    # 2. 재귀 호출
    # idx번 원소를 부분집합에 넣고 idx+1 번 원소를 판단하기
    selected[idx] = 1
    make_set(idx+1, selected, s+lst[idx])

    # idx번 원소를 부분집합에 넣지 않고 idx+1 번 원소를 판단하기
    selected[idx] = 0
    make_set(idx+1, selected, s+0)

# 0번부터 부분집합에 넣을지 말지 고민
make_set(0, [0]*N, 0)

# 원소의 개수가 C 개 이하인 부분집합만 출력해보기 연습
C = 2