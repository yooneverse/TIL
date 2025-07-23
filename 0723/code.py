"""동일 라인에 있는 것은 같은 선에서 실행가능하다고 이해하면 되는 것이고,
작은 범위에서 넓혀간다고 생각하면 되는 것. LEGB rule로 로컬-인접-글로벌-빌트인으로 기억하기

"""


x = 'G'
y = 'G'

def outer_func():
    x = 'E'
    y = 'E'

    def inner_func(y):  # 여기서 inner_func(y)로 하지 않고 다른 변수로 하면, 있는 곳에서 찾아오게 됨
        z = 'L'
        print(x,y,z)
    
    inner_func('F') # inner_func를 호출하면서 'F'라는 값을 인자로 전달. inner_func에서 지정한 y가 'F' 인자를 전달받아 F가 됨.
    print(x,y)
outer_func()
print(x,y)

packed_values = 1,2,3,4,5
print(packed_values)

def my_func(*args) : #args는 *을 활용한 패킹을 뜻하는 이름
    print(args)       
    print(type(args)) 

my_func(1,2,3,4,5) # 함수 호출

def my_func2(**kwargs) :
    print(kwargs)
    print(type(kwargs))
                          # 이 위 내용까지가 정의 부분
my_func2(a=1, b=2, c=3)    # 여기에서 함수호출을 하는 것. 따라서 호출되어야 하는 함수가 아래로 위치하는 것