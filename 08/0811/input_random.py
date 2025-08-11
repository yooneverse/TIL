# 파일명: input_random.py
import random
import time
import io
import sys

# ===== 문제 세트 (필요하면 자유롭게 추가/수정) =====
problems = [
    # --- Lv1: 기본 입력/출력 ---
    {"desc": "단일 정수 입력받아 출력", "input": "5", "output": "5",
     "solution": "n = int(input())\nprint(n)"},
    {"desc": "두 정수 입력받아 출력", "input": "3 7", "output": "3 7",
     "solution": "a, b = map(int, input().split())\nprint(a, b)"},
    {"desc": "세 정수 입력받아 출력", "input": "1 2 3", "output": "1 2 3",
     "solution": "a, b, c = map(int, input().split())\nprint(a, b, c)"},
    {"desc": "N개의 정수 입력받아 한 줄로 출력", "input": "4\n10 20 30 40", "output": "10 20 30 40",
     "solution": "n = int(input())\narr = list(map(int, input().split()))\nprint(*arr)"},
    {"desc": "문자열 입력받아 그대로 출력", "input": "Hello", "output": "Hello",
     "solution": "s = input()\nprint(s)"},
    {"desc": "문자열과 정수 입력받아 한 줄로 출력", "input": "Apple 3", "output": "Apple 3",
     "solution": "s, n = input().split()\nprint(s, n)"},
    {"desc": "공백 없는 숫자열 입력받아 각 자리 출력", "input": "1234", "output": "1 2 3 4",
     "solution": "num = input()\nprint(*num)"},
    {"desc": "정수 N, M 입력 후 N+M 출력", "input": "2 5", "output": "7",
     "solution": "n, m = map(int, input().split())\nprint(n + m)"},
    {"desc": "정수 N, M 입력 후 N*M 출력", "input": "3 4", "output": "12",
     "solution": "n, m = map(int, input().split())\nprint(n * m)"},
    {"desc": "실수 두 개 입력받아 합 출력", "input": "1.5 2.5", "output": "4.0",
     "solution": "a, b = map(float, input().split())\nprint(a + b)"},

    # --- Lv2: 2차원 배열, 조건문, 반복문 ---
    {"desc": "N x M 행렬 입력 후 그대로 출력", "input": "2 3\n1 2 3\n4 5 6",
     "output": "1 2 3\n4 5 6",
     "solution": "n, m = map(int, input().split())\nmat = [list(map(int, input().split())) for _ in range(n)]\nfor row in mat:\n    print(*row)"},
    {"desc": "N개의 정수 중 최댓값 찾기", "input": "5\n3 9 2 8 6", "output": "9",
     "solution": "n = int(input())\narr = list(map(int, input().split()))\nmax_val = arr[0]\nfor x in arr:\n    if x > max_val:\n        max_val = x\nprint(max_val)"},
    {"desc": "N개의 정수 중 최솟값 찾기", "input": "4\n5 2 7 1", "output": "1",
     "solution": "n = int(input())\narr = list(map(int, input().split()))\nmin_val = arr[0]\nfor x in arr:\n    if x < min_val:\n        min_val = x\nprint(min_val)"},
    {"desc": "1부터 N까지 합 출력", "input": "5", "output": "15",
     "solution": "n = int(input())\ntotal = 0\nfor i in range(1, n+1):\n    total += i\nprint(total)"},
    {"desc": "홀수만 합 출력", "input": "7\n1 2 3 4 5 6 7", "output": "16",
     "solution": "n = int(input())\narr = list(map(int, input().split()))\ntotal = 0\nfor x in arr:\n    if x % 2 == 1:\n        total += x\nprint(total)"},
    {"desc": "짝수만 합 출력", "input": "6\n2 4 6 8 10 12", "output": "42",
     "solution": "n = int(input())\narr = list(map(int, input().split()))\ntotal = 0\nfor x in arr:\n    if x % 2 == 0:\n        total += x\nprint(total)"},
    {"desc": "문자열 N개 입력 후 역순 출력", "input": "3\ncat\ndog\nbird", "output": "bird\ndog\ncat",
     "solution": "n = int(input())\nwords = [input() for _ in range(n)]\nfor w in reversed(words):\n    print(w)"},
    {"desc": "N x N 행렬 대각합 출력", "input": "3\n1 2 3\n4 5 6\n7 8 9", "output": "15",
     "solution": "n = int(input())\nmat = [list(map(int, input().split())) for _ in range(n)]\ntotal = 0\nfor i in range(n):\n    total += mat[i][i]\nprint(total)"},
    {"desc": "N x N 행렬 역대각합 출력", "input": "3\n1 2 3\n4 5 6\n7 8 9", "output": "15",
     "solution": "n = int(input())\nmat = [list(map(int, input().split())) for _ in range(n)]\ntotal = 0\nfor i in range(n):\n    total += mat[i][n-1-i]\nprint(total)"},
    {"desc": "리스트에서 특정 수의 개수 출력", "input": "5\n1 2 3 2 2\n2", "output": "3",
     "solution": "n = int(input())\narr = list(map(int, input().split()))\ntarget = int(input())\ncnt = 0\nfor x in arr:\n    if x == target:\n        cnt += 1\nprint(cnt)"},
    {"desc": "구구단 N단 출력", "input": "3", "output": "3 6 9 12 15 18 21 24 27",
     "solution": "n = int(input())\nfor i in range(1, 10):\n    print(n * i, end=' ')"}
]

# ===== 라운드 설정 =====
PER_ROUND = 5   # 한 회차당 문제 수

def ask_continue():
    try:
        ans = input("\n다음 회차로 진행할까요? (y/n): ").strip().lower()
    except EOFError:
        return False
    return ans == 'y'

def run_round(round_idx, batch):
    print(f"\n==== Round {round_idx} 시작 (총 {len(batch)}문제) ====")
    score = 0
    for idx, problem in enumerate(batch, 1):
        print(f"\n문제 {idx}/{len(batch)}")
        print(f"[설명] {problem['desc']}")
        print(f"[입력 예시]\n{problem['input']}")
        print(f"[출력 예시]\n{problem['output']}")

        try:
            input("준비되면 엔터를 누르세요...")
        except EOFError:
            print("\n(EOF 감지: 자동 진행)\n")

        print(">> 전체 코드를 작성하세요. 작성 완료 후 'END' 입력.")
        user_code_lines = []
        while True:
            try:
                line = input()
            except EOFError:
                print("\n(EOF 감지: 코드 입력 종료)\n")
                break
            if line.strip() == "END":
                break
            user_code_lines.append(line)

        user_code = "\n".join(user_code_lines).strip()

        # 빈 코드면 오답 처리 후 예시만 공개
        if not user_code:
            print("❌ 오답 (코드 없음)")
            print("\n--- 정답 예시 코드 ---")
            print(problem["solution"])
            print("-------------------")
            continue

        # 채점 실행
        start_time = time.time()
        captured_output = io.StringIO()
        sys_stdout_backup = sys.stdout
        sys_stdin_backup = sys.stdin
        sys.stdin = io.StringIO(problem["input"])
        sys.stdout = captured_output

        try:
            exec(user_code, {})
            user_output = captured_output.getvalue().strip()
        except Exception as e:
            user_output = f"Error: {e}"
        finally:
            sys.stdout = sys_stdout_backup
            sys.stdin = sys_stdin_backup

        time_taken = round(time.time() - start_time, 2)

        if user_output == problem["output"]:
            print(f"✅ 정답! ({time_taken}초)")
            score += 1
        else:
            print(f"❌ 오답 ({time_taken}초)")
            print("기대값:")
            print(problem["output"])
            print("네 출력:")
            print(user_output)

        print("\n--- 정답 예시 코드 ---")
        print(problem["solution"])
        print("-------------------")

    print(f"\n==== Round {round_idx} 결과: {score}/{len(batch)} ====")
    return score

def main():
    # 문제 풀 세팅 (중복 허용으로 30개 채움)
    pool = problems[:]
    while len(pool) < 30:
        pool.append(random.choice(problems))
    random.shuffle(pool)

    total_score = 0
    round_idx = 1
    start = 0

    print("=== 실전 input() 속도 퀴즈 (5문제/회) ===")

    while start < len(pool):
        batch = pool[start:start+PER_ROUND]
        if not batch: break
        total_score += run_round(round_idx, batch)
        start += PER_ROUND
        round_idx += 1
        if start >= len(pool):
            print("\n모든 문제를 풀었습니다. 수고했어요!")
            break
        if not ask_continue():
            print("\n훈련 종료!")
            break

    print(f"\n총합 점수: {total_score}/{min(len(pool), (round_idx-1)*PER_ROUND)}")

if __name__ == "__main__":
    main()

