# #1. 뒤집기

# def my_reverse(string):

# # string : 뒤집을 문자열

# # 뒤집은 결과
# result = ""

# # string의 맨 뒤에서부터 글자 하나씩 떼어와서 result에 올림

#     #string의 i번 인덱스에 있는 글자를 result에 붙이기


# # 뒤집은 결과 반환


# s = "Reverse this strings"


# # 주석만 보고 써보기


# #2. 회문

s = ["level", "refer", "mom", "pop", "abracadabra"]

# 어떤 문자열이 회문인지 아닌지를 return 하는 함수
def is_palindrome(txt):
    #문자열의 길이 N
    N = len(txt)

    # 비교를 N//2 번 만큼 하면 된다.
    # 중간에 다른 적이 한 번이라도 있다면 txt 회문이 아니다.
    # i의 범위는 0~N//2-1
    for i in range(N//2):
        #앞과 뒤가 같은지 다른지
        if txt[i] != txt[N-1-i]:
            # 다르면 회문이 아니다.
            return False
        
    # 여기까지 코드가 실행이 되면 중간에 달랐던 적이 없다 => 회문임
    return True

#s의 각 원소가 회문인지 아닌지
print(list(map(is_palindrome, s)))

