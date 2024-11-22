import random

your_credit = 2
computer_credit = 2

while( your_credit >0 and computer_credit >0) :
    number = random.randint(1,100)
    you = int(input("정수를 입력하세요."))

    if(number % 2 == you%2) :
        print("당신이 이겼습니다.")
        your_credit = your_credit +1
        computer_credit = computer_credit - 1
        
    else :
        print("당신이 졌습니다.")
        your_credit = your_credit -1
        computer_credit = computer_credit + 1

    print(f"생성된 랜덤 정수 : {number}")
    print(f"당신의 크래딧은 {your_credit}이고 컴퓨터의 크래딧은 { computer_credit}입니다. ")


'''
import random
number = random.randint(1,100)

you = int(input("정수를 입력하세요."))

if(number % 2 == you%2) :
    print("당신이 이겼습니다.")
else :
     print("당신이 졌습니다.")

print(f"생성된 랜덤 정수 : {number}")

'''
'''
import random
number = random.randint(1,100)

if(number % 2 == 0) :
    print("짝수입니다.")
else :
     print("홀수입니다.")

print(f"생성된 랜덤 정수 : {number}")
'''
'''
import random
number = random.randint(1,100)

print(f"생성된 랜덤 정수 : {number}")
  '''    

'''
number = 327

if(number % 2 == 0) :
    print("짝수입니다")

else :
    print("홀수입니다")
'''
'''
money = int(input("환전할 금액을 입력하세요."))
m_50000 = money // 50000 ; money_changes = money%50000
m_10000 = money_changes // 10000 ; money_changes = money%10000
m_5000 = money_changes // 5000 ; money_changes = money%5000
m_1000 = money_changes // 1000 ; money_changes = money%1000

print("오만원 : %d 장" %m_50000)
print("만원 : %d 장" %m_10000)
print("오천원 : %d 장" %m_5000)
print("천원 : %d 장" %m_1000)
print("지폐를 뺀 나머지 돈 : %d 원" %money_changes)
'''

'''
money = 2652
m_1000 = money // 1000
money_changes = money % 1000

print("천원 : %d 장" %m_1000)
print("천원 짜리를 뺀 나머지 돈 : %d장" %money_changes)
'''

'''
money = 7652
m_5000 = money // 5000
money_changes = money % 5000

print("오천원 : %d 장" %m_5000)
print("오천원 짜리를 뺀 나머지 돈 : %d장" %money_changes)
'''


'''
money = 37652
m_10000 = money // 10000
money_changes = money % 10000

print("1만원 : %d 장" %m_10000)
print("1만원 짜리를 뺀 나머지 돈 : %d장" %money_changes)
'''

'''
money = 187652
m_50000 = money / 50000
money_changes = money % 50000

print("5만원 : %d 장" %m_50000)
print("5만원 짜리를 뺀 나머지 돈 : %d장" %money_changes)
'''      

'''
a= 10 ; b =10 ;

if(a==b) :
    print("같다")
else :
    print("다르다")
    
'''
