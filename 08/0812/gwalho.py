T = int(input())

for tc in range(1, T+1):
    txt = input()  # 문자열 입력 받기
    N = len(txt)

    # 스택 만들기
    s = [0] * N  # 고정 스택
    top = -1
    answer = 1

    for i in txt:
        if i in '({':  # 여는 괄호
            top += 1
            s[top] = i
        elif i == ')':
            if top == -1 or s[top] != '(':
                answer = 0
                break
            top -= 1  # pop
        elif i == '}':
            if top == -1 or s[top] != '{':
                answer = 0
                break
            top -= 1  # pop

    if top != -1:  # 스택에 남은 여는 괄호가 있으면 실패
        answer = 0
    print(f"#{tc} {answer}")


T = int(input())

for tc in range(1, T+1):
    arr = input()




