T = 10

for tc in range(1, T + 1):
    N = int(input())  # 식의 길이
    infix = input()  # 중위표기식


# 스택 밖 우선순위(icp), 스택 안 우선순위(isp)
icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}


# 중위표기식을 후위표기식으로 변환
def get_postfix(infix: str, N: int) -> str:
    postfix = ""
    stack = []

    for token in infix:
        if token not in "()+-*/":
            # 피연산자면 그대로 추가
            postfix += token
        else:
            if token == "(":
                stack.append(token)
            elif token == ")":
                # '('를 만날 때까지 pop
                while stack and stack[-1] != "(":
                    postfix += stack.pop()
                if stack and stack[-1] == "(":
                    stack.pop()  # '(' 제거
            else:
                # 연산자: 스택 top과 우선순위 비교해 pop 후 push
                while stack and icp[token] <= isp[stack[-1]]:
                    postfix += stack.pop()
                stack.append(token)

    # 남은 연산자 전부 pop
    while stack:
        top = stack.pop()
        if top != "(":
            postfix += top

    return postfix


# 후위표기식 계산
def get_result(postfix: str) -> int:
    stack = []
    for token in postfix:
        if token not in "+-*/":
            # 숫자(한 자리) => token 하나씩 받아오니까
            stack.append(int(token))
        else:
            # 주의: pop 순서 (먼저 꺼낸 게 오른쪽)
            right = stack.pop()
            left = stack.pop()

            if token == '+':
                stack.append(left + right)
            elif token == '-':
                stack.append(left - right)
            elif token == '*':
                stack.append(left * right)
            elif token == '/':
                # 정수가 주어지기 때문에 // 사용
                stack.append(left // right)
    return stack.pop()

    postfix = get_postfix(arr, N)
    result = get_result(postfix)

    print(f"#{tc} {result}")