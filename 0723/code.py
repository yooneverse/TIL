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

