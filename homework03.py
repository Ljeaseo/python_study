"""
DocString
세번째 파이썬 파일입니다.
2022.08.23. by coc_o_pus
"""


class 붕어빵틀():
    def __init__(self, 앙꼬):
        print("생성자")
        self.앙꼬 = 앙꼬    
if __name__=="__main__":
    print("이것이 파이썬 기본 골격입니다.")
    
    붕어빵1 = 붕어빵틀("팥")
    붕어빵2 = 붕어빵틀("크림")
    
    print(붕어빵1.앙꼬)
    print(붕어빵2.앙꼬)
    
str1 = ['h','e','l','l','o']
str2 = 'hello'
print(str1,'\n',str2)
str2 = list(str2)
print(str1,'\n',str2)

import math
n = input("")

if  n == 2 :
    print("같다.")
else :
    print("다르다.")