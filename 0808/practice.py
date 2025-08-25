#4. 첫줄에 N, N*N 문자열이 들어온 경우

N = int(input())
text = [input() for _ in range(N)]

# 패턴의 크기
P = 2

pat = [ "AB" , "CD"]

# # 텍스트에 배당한 번호와 패턴의 번호가 같은가를 검토하기를 반복

print(text, pat)

# 패턴이 큰 2차원배열(사각형) 안에 존재하나요? => 없다고 가정
answer = "NO"

# 큰 사각형 안에 작은 사각형 영역 만들어서 검사
# 영역 행 좌표(i), 열 좌표(j)의 범위로 나타내기
for i in range(N-P+1):
    for j in range(N-P+1):
        # (i,j)에서 시작해서 2*2 작은 사각형 영역

        #"큰 사각형 안에" 만들 작은 사각형 패턴과 비교할 작은 사각형 패턴이 같다고 가정
        flag = True
        # di(i 변화량 (!=델타)) 의 범위 : 0~1
        # dj(j 변화량)의 범위 : 0~(P-1)
        # di, dj 는 작은 패턴의 인덱스로도 사용 가능
        for di in range(P):
            for dj in range(P):
                # 패턴과 큰 사각형의 작은 부분 비교
                if pat[di][dj] != text[i+di][j+dj]:
                    # 전부 다 있다고 생각하였기에, 하나라도 없는 것을 찾으면 충족되지 않는 것 (하나라도 다르면 패턴 불일치)
                    flag = False

        # 비교했을 때 False가 없기에, 아직도 flag == True라는 것
        # if flag == True:
        if flag:
            answer = "YES"

print(answer)