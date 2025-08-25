lst = [1,2,3]
N = 3

# 자리의 주인을 지목하는 방식
# 완성된 순열의 길이도 3
# 0번 인덱스에 누가 오나: make_perm(0)
# 1번 인덱스에 누가 오나: make_perm(1)
# ...

# N-1번 인덱스에 누가 오나: make_perm(N-1)
# N번 인덱스에 누가 오나 => 안 됨, 재귀 중단 : make_perm(N)
# idx : 완성된 순열의 idx번 자리에 사용할 원소 선택
# selected : 순열을 만들때 이전에 사용한 원소는 사용불가, 체크용
# selected[x] = 1 : x번 원소는 이전에 순열 만들 때 사용했다는 것
# selected[y] = 0 : y번 원소는 이전에 순열 만들 때 사용하지 않았고 => idx 자리에 y번 원소가 올 수 있음
# result: idx단계까지 완성된 순열(기억해두는 곳) _ 리스트로 만들거나, 문자열로 만들기
def make_perm(idx, selected, result):

    # 1. 종료 조건
    if idx == N:
        print(result)
        return

    # 2. 재귀 호출
    # idx 번 자리에 누가 오는가 선택
    # N 개 중에 하나 선택할 건데 => 이전에 선택한 적 있는 원소는 선택하면 안 된다
    # result.append(0)
    # make_perm(idx+1)
    #
    # result.append(1)
    # make_perm(idx + 1)
    #
    # result.append(2)
    # make_perm(idx+1)
    # 위처럼 일일히 하면 안 되고
    # 반복문 써서 처리해야 함(모든 테스트 케이스에 맞도록)

    for i in range(N):
        # i번 원소를 이전에 순열 만들 때 쓴 적 없다면 => 순열의 idx번 위치에 올 수 있음
        if not selected[i]:
            # 순열의 idx번 자리에 i번 원소를 놓고 idx+1번 자리에 누가 올지 고민
            selected[i] = 1
            # 순열 만들기, lst의 i번 원소 사용
            result.append(lst[i])
            make_perm(idx+1, selected, result)

            # 한 번 차례 마치면 복구하는 과정을 넣어줘야 함
            # i번 원소를 idx 자리에 놓은 경우의 수는 모두 고려 완료
            # i+1qjs 원소를 놓기 시작, i번 원소는 사용하지 않았다로 고쳐야 함
            selected[i] = 0
            result.pop()

# 0번 자리에 누가 올지, 아직 아무도 고른 적 없고, 순열은 미완성인 상태(빈 상태)로 시작
make_perm(0,[0]*N, [])