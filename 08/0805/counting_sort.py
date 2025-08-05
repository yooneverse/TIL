def counting_sort(DATA, TEMP, K):
    # DATA : 정렬하고싶은 대상(배열, 리스트)
    # TEMP : 정렬 결과(배열, 리스트)
    # K : 정렬 대상 배열 안에 들어있는 정수 중 최대값
    # K == 카운트 배열의 크기

    COUNT = [0] * (K + 1)
    # COUNT : 카운트배열(각 원소의 등장 횟수를 세기 위해)
    # C[X] : 정수 X의 등장 횟수
    # C[3] : 숫자 3이 DATA배열 안에 몇개 있었는지 기록

    # 1. 모든 원소의 등장 횟수를 카운트
    for num in DATA:
        # DATA 배열 안에서 꺼내온 숫자 num의 등장횟수 +1
        COUNT[num] += 1

    # 2. 각 원소의 등장횟수를 더해서 누적 합 계산
    # 각 원소가 정렬후에 들어갈 자리 위치를 계산
    # 어떤 숫자 x 보다 작은 숫자가 몇개 있는지 알고 있다면
    # x의 정렬 후 자리를 특정할 수 있다.
    for i in range(1, K + 1):
        COUNT[i] = COUNT[i] + COUNT[i - 1]

    # 3. 뒤에서부터 DATA를 확인하면서 COUNT배열을 보고
    # 자리를 확인, 자리(인덱스) = COUNT[숫자] - 1
    # COUNT[X] 에 가서 값 확인하고 여기서 -1 한 위치(인덱스)
    # 정렬 후 위치가 된다.
    # 뒤에서 부터 확인하는 이유는? 안정 정렬을 위해서(원래 순서를 보장)
    for i in range(len(DATA) - 1, -1, -1):
        # DATA[i] 에 있는 숫자의 정렬 후 위치는 어딘가요???
        # COUNT 에서 DATA[i] 에 있는 숫자의 값을 확인, -1 한 자리가 정렬후 위치
        x = DATA[i]
        COUNT[x] -= 1

        # 정렬후 결과 배열 TEMP에 DATA[i] 놓기
        # x : DATA[i]
        # COUNT[x] : x(DATA[i])가 들어갈 위치(인덱스)
        TEMP[COUNT[x]] = x


nums = [0, 4, 1, 3, 1, 2, 4, 1]  # 정렬 대상 배열
result = [0] * 8  # 정렬 결과

counting_sort(nums, result, max(nums))
print(result)
