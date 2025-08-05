# #답을 나타낼 변수를 만들고, 예외 경우가 주어질 경우 그 값으로 초기화를 해놓으면 좋음
# #만족하지 못하면 초기화 된 값으로 가게 하면 되기 때문
#
# stop = [0] * N
# stop[1] = 1 #있으면 1, 없으면 0
# #범위를 생각해낼 수 없다면 while문 사용에 익숙해져야 함.
#
# #입력은 한 줄씩, 한 줄당 무조건 input이 있어야 함.

T = int(input())


def drive(K, N):


# K = 한 번 충전 시 이동 가능한 정류장 개수
# N = 마지막 도착 정류장 번호

# return값 == 0 : 버스가 마지막 정류장에 도착하지 못함
# return값 > 0: 버스가 마지막 정류장에 도착함
# return으로 함수 즉시 종료 가능
    last = 0 # 마지막 충전 위치
    bus = K # 버스가 최대로 움직인 위치(초기값은 한번 최대로 이동)
    count = 0 #충전 횟수, 시작 충전은 횟수 제외

    #버스 위치가 N보다 작으면 계속 움직여라.
    while bus < N:
        # 현재 위치에 충전기가 있는지 확인
        # 없으면 다시 한 칸씩 돌아오기
        # if stop_list[bus] == 1:
        #     # 다시 뛰기
        # else:
        #     # 한 칸씩 돌아오기

        while stop_list[bus] == 0:
            bus -= 1
            #마지막에 충전한 위치로 돌아와 버리면 운행 불가!!
            if bus == last:
                return 0

        # stop_list[bus] == 1인 곳을 만나면 반복 중단
        # 더 갈 수 있음을 의미
        # 마지막 충전 위치를 현재 위치로 저장(기록)
        last = bus
        # 충전했으니 충전횟수 +1
        count += 1
        # 충전했으니 K칸 쭉 옮김
        bus += K

# 반복이 종료되면 충전횟수 return
    return count

for tc in range(1, T + 1):
    # tc는 테스트 케이스 번호, 1부터 시작

    # 입력이 한 줄에 3개가 들어온다는 게 고정이면
    # 변수도 3개 준비해놓으면 된다.
    K, N, M = map(int, input().split())
    # K = 1번 충전 시 이동가능한 정류장 수
    # N = 마지막 도착 정류장 번호
    # M = 충전기 개수

    # 충전기가 있는 정류장 번호 리스트
    charger_list = list(map(int, input().split()))

    # 정류장 리스트
    stop_list = [0] * N
    # stop_list[1] == 1 : 충전기 보유
    # stop_list[2] == 0 : 충전기 보유

    # 충전기가 있는 정류장 번호 확인
    for x in charger_list:
        # x번 정류장에는 충전기 있다고 표시
        stop_list[x] = 1

    answer = drive(K,N)
    print(answer)


