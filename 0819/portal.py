# x 번 방에 처음 도착했을 때 y번 방으로 이동하는 포탈이 존재하는지
# potals[x] : x번 방에 처음 도착했을 때 이 방에 있는 포탈을 사용하면
# portals[x]-1 (인덱스와 맞춰주기 위해서) 번 방으로 이동한다
# portals[x] == 0 : x번 방은 이전에 사용했거나 첫번째 방임
# 바로 x+1번 방으로 이동하는 포탈 사용

portals = list(map(int, input().split()))

# visited = [0] * N
# 현재 위치
idx = 0

# 포탈 이용 횟수
count = 0

# 반복을 정확히 몇 번 해야 할지 모르겠으면 while 사용
# 현재 방 번호가 마지막 방 번호보다 작으면
while idx < N-1:
    # idx 번 방에 있는 포탈 확인

    # idx 번 방을 처음 방문했을 때
    # 이 방에 쓰인 번호가 0이 아니면 그 번호 방으로 이동
    if portals[idx] != 0:
        # idx 방에 처음 방문했기 때문에, 방번호를 저장
        # 인덱스와 맞추기 위해 -1
        jump_to = portals[idx]-1
        # idx번 방을 방문했다는 표식으로
        portals[idx] = 0
        # 포탈 사용 후 위치 갱신
        idx = jump_to
        # 포탈 사용횟수 갱신
        count += 1
        # idx 번 방을 두 번 이상 방문했을 때
    else:
        # 오른쪽 방으로 이동
        idx += 1
        # 포탈 사용횟수 갱신
        count += 1

    print(f"#{tc} {count}")




