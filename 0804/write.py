# def counting_sort(DATA, TEMP, k):
#     # DATA : 정렬하고 싶은 대상(배열, 리스트)
#     # TEMP : 정렬 결과(배열, 리스트)
#     # K : 정렬 대상 배열 안에 들어있는 정수 중 최대값
#     # K == 카운트 배열의 크기

#     COUNT = [0] * (k+1)
#     # COUNT : 카운트배열 (각 원소의 등장 횟수를 세기 위해)
#     # C[X] : 정수 X 등장 횟수
#     # C[3] : 숫자 3이 DATA배열 안에 몇 개 있었는지 기록

#     #1. 모든 원소의 등장 횟수를 카운트
#     #for i in range (len(DATA))
#     for num in DATA:
#         #DATA 배열 안에서 꺼내온 숫자 num의 등장횟수 +1
#         COUNT[num] += 1 #원소의 발생횟수를 기록함

#     #2. 각 원소의 등장횟수를 더해서 누적 합 계산
#     # 각 원소가 정렬후에 들어갈 자리 위치 계산
#     # 어떤 숫자 X 보다 작은 숫자가 몇 개 있는지 알고 있다면
#     # X의 정렬 후 자리를 특정할 수 있음
#     for i in range(1, k+1):
#         COUNT[i] = COUNT[i] + COUNT[i-1]

#     #3. 뒤에서부터 DATA 확인하면서 COUNT배열을 보고
#     # 자리를 확인, 자리(인덱스) = COUNT[숫자] - 1
#     # COUNT[X]에 가서 값 확인하고 여기서 -1한 위치(인덱스)
#     # 정렬 후 위치가 된다.
#     # 뒤에서부터 확인하는 이유는? 안정 정렬을 위해서 ( 원래 순서를 보장하는 정렬을 안정 정렬이라고 함 )
#     for i in range(len(DATA)-1, -1, -1):
#         # DATA[i]에 있는 숫자의 정렬 후 위치는 어딘가?
#         # COUNT에서 DATA[i]에 있는 숫자의 값을 확인, -1 한 자리가 정렬 후 위치
#         x = DATA[i]
#         COUNT[x] -= 1

#         # 정렬 후 결과 배열 TEMP에 DATA[i] 놓기
#         # x = DATA[i]
#         # COUNT[x] : x(DATA[i])가 들어갈 위치(인덱스)
#         TEMP[COUNT[x]] = x

# nums = [0, 4, 1, 3, 1, 2, 4, 1] # 정렬 대상 배열
# result = [0] * 8  #정렬 결과
# print(nums)


T = 10  # 테스트케이스 수
 
# tc : test_case
for tc in range(1, T + 1):
    dump_cnt = int(input())  # 평탄화할 덤프 횟수
    heights = list(map(int, input().split()))  # 100개의 상자 높이를 리스트로 입력받음
 
    # 높이가 0부터 100까지 있을 수 있으므로 크기 101짜리 배열 생성
    # cnt[h]는 '높이 h를 가진 상자의 개수'를 의미함
    MIN_HEIGHT = 1
    MAX_HEIGHT = 100
    cnt = [0] * (MAX_HEIGHT + 1)

 
    # 입력받은 높이들을 카운팅 배열에 반영
    for height in heights:
        cnt[height] += 1
 
    # 정해진 횟수만큼 평탄화 수행
    for _ in range(dump_cnt):
 
        # 최소 높이(left) 찾기
        # 카운팅 배열은 왼쪽에서 오른쪽으로 높이가 커지므로,
        # cnt[left] > 0인 가장 작은 left가 최소 높이
        left = 0
        while cnt[left] == 0:
            left += 1
 
        # 최대 높이(right) 찾기
        # 카운팅 배열은 오른쪽에서 왼쪽으로 높이가 작아지므로,
        # cnt[right] > 0인 가장 큰 right가 최대 높이
        right = 100
        while cnt[right] == 0:
            right -= 1
 
        # 이미 평탄화가 완료된 경우: 최대 - 최소 <= 1이면 종료
        if right - left <= 1:
            break
 
        # 평탄화 작업 수행
        # -> 가장 높은 곳에서 상자 하나 빼서 가장 낮은 곳 위에 놓기
        # -> 높이 차이를 줄이기 위한 전략
        cnt[left] -= 1         # 가장 낮은 위치에서 상자 1개 제거
        cnt[left + 1] += 1     # 그보다 한 칸 높은 위치에 추가
 
        cnt[right] -= 1        # 가장 높은 위치에서 상자 1개 제거
        cnt[right - 1] += 1    # 그보다 한 칸 낮은 위치에 추가
 
    # 덤프가 끝난 후, 다시 최종 최대/최소 높이를 계산
    left = 0
    while cnt[left] == 0:
        left += 1
 
    right = 100
    while cnt[right] == 0:
        right -= 1
 
    # 결과 출력: 최댓값 - 최솟값
    print(f"#{tc} {right - left}")