# T = int(input())  # 테스트케이스 개수 (1 ≤ T ≤ 50)
#
# for tc in range(1, T + 1):
#     # 문자열 1줄 읽어와서 저장
#     arr = input()
#     N = len(arr)
#
#     # 스택 사용 (방법2)
#     s = [0] * N  # 고정 크기 스택
#     top = -1     # 스택 초기화
#
#     # 스택에 첫 글자 push
#     top += 1
#     s[top] = arr[0]
#
#     # 1번 인덱스(0번은 위에서 넣었음)부터 입력받은 문자열 순회
#     for i in range(1, N):
#         # 스택의 마지막 원소(top, 꼭대기) 와 현재 순회하는 문자와 같은지 비교
#         if s and s[top] == arr[i]:
#             # 같다면 스택에서 같은 문자 pop
#             top -= 1 #고정 스택이니까
#         else:
#             # 다르다면 현재 순회 문자열 스택에 push
#             top += 1
#             s[top] = arr[i]
#
#     # 반복 종료 후 스택의 길이 출력
#     print(f"#{tc} {top+1}")

T = 10  # 테스트케이스 개수 고정

for tc in range(1, T + 1):

    # 문자 총 수와 문자열을 공백 기준으로 분리해서 받기
    N, arr = input().split()
    N = int(N)  # 문자 총 수 정수 변환

    # 스택 초기화 (고정 크기)
    s = [0] * N
    top = -1

    # 스택에 첫 글자 push
    top += 1
    s[top] = arr[0]

    # 1번 인덱스부터 문자열 순회하면서 짝 찾기
    for i in range(1, N):
        if s and s[top] == arr[i]:  # 스택이 비어있지 않고 top 값이 현재 문자와 같다면
            top -= 1  # pop
        else:
            top += 1  # push
            s[top] = arr[i]

    # 스택의 남은 값만 잘라서 문자열로 변환
    # top이 -1이면 빈 문자열, 아니면 join
    result = ''.join(s[:top + 1])
    print(f"#{tc} {result}")


  # 스택의 남은 값만 잘라서 문자열로 변환
    # top이 -1이면 빈 문자열, 아니면 join
    result = ''.join(s[:top + 1])
