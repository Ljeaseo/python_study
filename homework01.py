import math

"""
DocString
첫번째 파이썬 파일입니다.
2022.08.19. by coc_o_pus
"""
"""
a = 100
b = 200
sum = a + b
print("abc"+"abc"+"abc")
print("abc","abc","abc")
print("합 : ",sum)
print("합 : %d"%sum)
print("합:{0}+{1}={2}".format(a,b,sum))
print(f"합 : {a}+{b} = \n {sum}")
#\n : 탈출문자(escape sequence), \t ,\b, \\, %%
print(r"합 : {a}+{b} = \n {sum}") # raw format

# 윈도우+v -> ctrl+c로 복사해둔거 클립보드로 한번에 확인 가능!

"""

# num1=int(input("첫번째 숫자를 입력하세요 >>"+ ""))
# num2=int(input("두번째 숫자를 입력하세요 >>"+ ""))
# val = num1-num2
# print(val)


a = 10
b = 10
theta = 45

s = 1/2 * a * b * math.sin(math.pi * (theta/180))
print(f"넚이 : {s:.2f}") # {출력값 : .2f-> 소숫점 두자리까지 }