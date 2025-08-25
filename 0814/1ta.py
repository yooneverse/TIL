start = (1,1)
end = (2,2)

a = abs(end[0] - start[0]) # x 좌표의 차이
b = abs(end[1] - start[1]) # y 좌표의 차이

r = math.sqrt(a**2+b**2)

# 아크탄젠트는 math.atan 함수를 이용하면 계산할 수 있음
# math.atan의 결과는 radian으로 나옴 (degree가 아님)
radian = math.atan(b/a)

# radian을 degree로 변경을 해야 실제 각도를 얻을 수 있음
print(r.math.degrees(radian))