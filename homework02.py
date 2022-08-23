"""
DocString
두번째 파이썬 파일입니다.
2022.08.22. by coc_o_pus
"""
import math


# 한글변수명이 가능.
a = 3
print(a)
에이 = 3
print(에이) 

# 원 면적 구하기
반지름 = float(input("반지름을 입력하세요 :"+"")) 


둘레 = float(2 * math.pi * 반지름)  
면적 = float(math.pi * 반지름 ** 2) 

print(f'둘레:{둘레:.2f}, 면적:{면적:.2f}')

# 입력값의 타입 출력
print(type(1))
print(type(1.2))
print(type(True))
print(type(3+4j))
print(type('문자열'))
print(type('a'))
print(type(2<3))
print(type((1,2,3)))
print(type({1,2,3}))
print(type([1,2,3]))


# 파이썬은 정수의 끝이 없다. 
num = 99999999999999999999999999999999999999999
print(num)

#16진수
a = 0xFF
#8진수
b = 0o77
#2진수
c = 0b1111

print(a,b,c)