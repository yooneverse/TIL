# '''
# (6+5*(2-8)/2)
# 6528-*2/+
# '''

# stack = [0] * 10
# top = -1
# icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
# isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}

# infix = '(6+5*(2-8)/2)'
# postfix = ''

# for token in infix:
#     if token not in '(+-*/)': # 피연산자이면 후위식에 추가
#         postfix += token
#     elif token == ')': # 여는 괄호를 만날 때까지 pop
#         while top>-1 and stack[top] != '(':
#             top -= 1
#             # tmp = stack[top+1]
#             postfix += stack[top+1]
#         if top != -1:
#             top -= 1   # '(' 버림
    
#     else:
#         if top==-1 or isp[stack[top]] < icp[token]: #토큰의 우선순위가 더 높으면
#             top += 1    # push
#             stack[top] = token
#         elif isp[stack[top]] >= icp[token]: # 토큰과 같거나 더 높으면
#             while top > -1 and isp[stack[top]] >= icp[token]:
#                 postfix += stack[top]
#                 top -= 1
#             top += 1  # push
#             stack[top] = token

# print(postfix)

'''
우리 반 강사님 코드
'''

# 스택 밖에 있을 때 우선순위
icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
# 스택 안에 있을 때 우선순위
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}

# 중위표기식을 후위표기식으로 바꾸기
# infix : 중위표기식
# N : 식의 길이(토큰 개수)
def get_postfix(infix, N):
    # 결과로 출력할 후위표기식
    postfix = ""
    stack = []

    # 중위표기식에서 글자(토큰) 하나씩 떼어와서 후위표기식을 만들자
    for token in infix:
        # 연산자인지 피연산자인지 확인
        # 토큰이 피연산자인 경우
        if token not in "()+-*/":
            # 후위표기식에 그대로 피연산자를 쓴다 (출력한다)
            postfix += token
        # 토큰이 연산자인 경우
        else:
            #")"라면
            if token == ")":
                #"(...)" 안에 있는 모든 연산자가 먼저 계산이 되어야 한다
                # 스택 안에 "("를 만날 때까지 모든 연산자를 꺼내 쓴다.
                while stack:
                    operator = stack.pop()
                    # 꺼낸 게 "("라면 연산자 꺼내기 중단
                    if operator == "(":
                        break
                    # 여는 괄호가 아니면 계속 식에 출력
                    postfix += operator
            # 토큰이 닫는 괄호가 아닌 다른 연산자였다면
            else:
                # 스택 꼭대기에 있는 연산자의 우선순위와 => isp
                # 현재 토큰의 우선순위를 비교 => icp[token]
                # 누가 더 우선순위가 높은지 확인
                # 우선순위가 높은 연산자는 먼저 계산이 되어야 하니까 출력하기
                
                # 스택 안에 현재 token 보다 우선순위가 같거나 높은 연산자는 다 꺼내 쓴다
                while stack and icp[token] <= isp[stack[-1]]:
                    # 꺼내서 결과에 이어붙이기
                    postfix += stack.pop()

                # 토큰의 우선순위가 스택의 꼭대기에 있는 연산자의 우선순위보다 높았다면
                # 또는 스택이 비어있다면
                stack.append(token)

    # 모든 토큰을 확인 한 후에 스택에 남아있는 연산자는 그대로 차례대로 출력
    while stack:
        postfix += stack.pop()

    return postfix

infix = "(6+5*(2-8)/2)"
postfix = get_postfix(infix, len(infix))
print(postfix)

def get_result(postfix):
    # 계산 방법
    # 토큰을 하나씩 쭉 읽음
    # 연산자를 만나면 제일 최근에 만난 피연산자 두 개 가지고 연산
    # 스택에 피연산자를 저장

    stack = []

    for token in postfix:
        # 토큰 하나 떼어와서

        # 피연산자라면
        if token not in "X/+-":
            stack.append(int(token)) # 타입을 조심!!

        # 연산자라면
        else:
            # 스택에서 두 개 꺼내서 연산하고 그 결과값을 다시 스택에 넣기
            # 꺼내는 순서에 따라 연산자의 왼쪽인지 오른쪽인지
            # 먼저 꺼낸 게 오른쪽
            right = stack.pop()
            left = stack.pop()

            # 연산자 종류에 따라 계산
            result = 0

            if token == '+':
                result = left+right
            elif token == "-":
                result = left-right
            elif token == "*":
                result = left*right
            elif token == "/":
                result = left/right # 연산 결과 정수? 실수?

            # 이 계산 결고도 나중에 연산자의 피연산자로 사용될 것
            stack.append(result)

    # 계산이 잘 진행되었다면 모든 토큰을 읽고 난 후에
    # 스택안의 상태가?
    # 잘 표현되었다면 계산하고, 아니면 에러라고 판단해주세요 라는 문제 출제 가능
    return stack.pop()

result = get_result(postfix)
print(result)
