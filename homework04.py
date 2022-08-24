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