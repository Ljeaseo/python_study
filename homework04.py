"""
DocString
네번째 파이썬 파일입니다.
2022.08.24. by coc_o_pus
"""
# Vscode 폰트 설정
# 관리 -> 설정 -> 사용자탭 -> Font Family -> 'Source Code Pro' 입력

'''
class 붕어빵틀():
    여기는클래스변수 = 0
    공유변수 = 0 
       
    def __init__(self, 앙꼬):
        print("생성자")
        self.여기는인스턴스변수 = 0
        self.앙꼬 = 앙꼬
        
if __name__=="__main__":
    print("이것이 파이썬 골격입니다.")
    
    붕어빵1 = 붕어빵틀("팥")
    붕어빵2 = 붕어빵틀("크림")
    붕어빵3 = 붕어빵틀("치즈크림")

    print(붕어빵1.앙꼬)
    print(붕어빵2.앙꼬)
    print(붕어빵3.앙꼬)
    print(붕어빵틀.공유변수)
    붕어빵1.공유변수 = 100
    print(붕어빵1.공유변수)
    
    붕어빵틀.공유변수 = 100
    print("붕어빵1.공유변수:",붕어빵1.공유변수)
    print("붕어빵2.공유변수:",붕어빵2.공유변수)
    붕어빵1.공유변수 = 5
    
    
    
    
    
    a = 0b1
    
    for i in range(1,5):
        print(a<<i)
        
    data01 = 0b110000
        
    print("data01",data01)
    
    data01 >>= 1
    
    print("data01",data01)
'''     
#비트 왼쪽을 1씩 이동하면 *2 , 오른쪽으로 1씩 이동하면 /2






# list = []
# sum = 0
# for i in range(3):
#     list.append(int(input("점수를 입력하세요.")))
#     sum+=list[i]
#     avg = sum/list[i]
# print("총점 :",sum,"평균 :",avg.f2)
'''
from random import random


if __name__ == "__main__":
    
    myList = []

    myList.append(80)
    myList.append(90)
    myList.append(100)
    myList.insert(0,50)
    myList.insert(2,35)

    total = sum(myList)
    print(len(myList))

    avg = total / len(myList)

    print(f'총점 {total}, 평균 {avg:.2f}')
'''

'''
import random
import os

trys = 0
answers = 0

while True:

    # 값 생성
    num1 = random.randint(0,10)
    num2 = random.randint(0,10)

    print(f"{num1} + {num2} = ")
    result = int(input("덧셈의 값은?"))
    
    if(result == num1+num2):   #정답일때
        print("정답입니다.")
        answers += 1
        trys += 1
    else:                      #오답일때
        print("오답입니다.")    
        trys += 1
    
    #문제를 더 풀지 말지 선택후 터미널 clear 
    stop = int(input("그만하고 싶으면 0, 더하고 싶으면 1"))
    os.system('cls')  
    
    #문제를 풀지 않겟다고 선택했을 때
    if(stop == 0):
        print(f"시도횟수 : {trys}, 맞은 횟수: {answers}")
        break
''' 


#물건값 입력
price = int(input("물건의 값을 입력하세요:"))
#지불한 금액
pay = int(input("지불할 금액을 입력하세요:"))

#거스름돈
change = pay-price
print(change)

money1000 = change//1000
change = change%1000

money500 = change//500
change = change%500

money100 = change//100
change = change%100

money10 = change//10
change = change%10 

print(f"거스름돈은:{change}, 천원짜리는{money1000}장, 오백원짜리는{money500}개,백원짜리는{money100}개,십원짜리는{money10}개")








    
        
    
 
    
    

    
    