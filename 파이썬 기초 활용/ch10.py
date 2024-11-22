
while(True) :
    money_temp = input("환전할 금액을 입력하세요.")

    if not money_temp.isnumeric( ) :
        print("정수가 아닙니다.다시 입력하세요.")
        continue
    money = int(money_temp)
    break

while(True) :
    dollar_temp = input("환율을 입력하세요.")

    if not dollar_temp.isnumeric( ) :
        print("정수가 아닙니다.다시 입력하세요.")
        continue
    dollar = int(dollar_temp)
    break

dollar_100 = money // (dollar*100)
money_return = money % (dollar*100)

dollar_10 = money_return // (dollar*10)
money_return = money % (dollar*10)

dollar_5 = money_return // (dollar*5)
money_return = money_return % (dollar*5)

dollar_1 = money_return // (dollar)
money_return = money_return % (dollar)

print(f"백달러 지폐는 {dollar_100}장 입니다. ")
print(f"십달러 지폐는 {dollar_10}장 입니다. ")
print(f"오달러 지폐는 {dollar_5}장 입니다. ")
print(f"일달러 지폐는 {dollar_1}장 입니다. ")
print(f"돌려받은 한화는 {money_return}원 입니다. ")
print(f"1 dollar는 {dollar}원 입니다. ")

'''
money = int(input("환전할 금액을 입력하세요."))
dollar = int(input("환율을 입력하세요."))

dollar_100 = money // (dollar*100)
money_return = money % (dollar*100)

dollar_10 = money_return // (dollar*10)
money_return = money % (dollar*10)

dollar_5 = money_return // (dollar*5)
money_return = money_return % (dollar*5)

dollar_1 = money_return // (dollar)
money_return = money_return % (dollar)

print(f"백달러 지폐는 {dollar_100}장 입니다. ")
print(f"십달러 지폐는 {dollar_10}장 입니다. ")
print(f"오달러 지폐는 {dollar_5}장 입니다. ")
print(f"일달러 지폐는 {dollar_1}장 입니다. ")
print(f"돌려받은 한화는 {money_return}원 입니다. ")
print(f"1 dollar는 {dollar}원 입니다. ")
'''

'''
money = int(input("환전할 금액을 입력하세요."))
dollar = 1146

dollar_100 = money // (dollar*100)
money_return = money % (dollar*100)

dollar_10 = money_return // (dollar*10)
money_return = money % (dollar*10)

dollar_5 = money_return // (dollar*5)
money_return = money_return % (dollar*5)

dollar_1 = money_return // (dollar)
money_return = money_return % (dollar)

print(f"백달러 지폐는 {dollar_100}장 입니다. ")
print(f"십달러 지폐는 {dollar_10}장 입니다. ")
print(f"오달러 지폐는 {dollar_5}장 입니다. ")
print(f"일달러 지폐는 {dollar_1}장 입니다. ")
print(f"돌려받은 한화는 {money_return}원 입니다. ")
print(f"1 dollar는 {dollar}원 입니다. ")
'''
'''
money = 83200
dollar = 1146

dollar_10 = money // (dollar*10)
money_return = money % (dollar*10)

dollar_5 = money_return // (dollar*5)
money_return = money_return % (dollar*5)

dollar_1 = money_return // (dollar)
money_return = money_return % (dollar)

print(f"십달러 지폐는 {dollar_10}장 입니다. ")
print(f"오달러 지폐는 {dollar_5}장 입니다. ")
print(f"일달러 지폐는 {dollar_1}장 입니다. ")
print(f"돌려받은 한화는 {money_return}원 입니다. ")
print(f"1 dollar는 {dollar}원 입니다. ")
'''
'''
money = 1000000
dollar = 1146

dollar_100 = money // (dollar*100)
money_return = money % (dollar*100)

print(f"백달러 지폐는 {dollar_100}장 입니다. ")
print(f"돌려받은 한화는 {money_return}원 입니다. ")
print(f"1 dollar는 {dollar}원 입니다. ")
'''
'''
import random
game = 3
win = 0
lose = 0

while(game) :
    number = random.randint(1,100)
    
    while(True) :
        you = input("정수를 입력하세요.")
        if not you.isnumeric( ) :
            print("정수가 아닙니다.")
            print("정수를 입력하세요.")
            continue
        break
    
    game = game-1
    you_number = int(you)

    if(number % 2 == you_number%2) :
        print("당신이 이겼습니다.")
        win = win+1
    else :
        print("당신이 졌습니다.")
        lose = lose+1

    print(f"생성된 랜덤 정수 : {number}")
    print(f"{win}승 {lose}패입니다.")

'''


'''
import random
number = random.randint(1,100)

while(True) :
    you = input("정수를 입력하세요.")

    if not you.isnumeric( ) :
        print("정수가 아닙니다.")
        print("정수를 입력하세요.")
        continue 
    break         

you_number = int(you)

if(number % 2 == you_number%2) :
    print("당신이 이겼습니다.")
else :
     print("당신이 졌습니다.")

print(f"생성된 랜덤 정수 : {number}")
'''

'''
a=0

if(a) :
    print(" 참입니다.   ")
    print(" 진짜 참입니다.   ")
    print(" 진짜 진짜 참입니다.   ")

else :
    print(" 거짓입니다.   ")
    print(" 진짜 거짓입니다.   ")
    print(" 진짜 진짜 거짓입니다.   ")
  '''  
'''
a = 0

if(a) :
    print("참입니다.")
else :
    print("거짓입니다.")

'''
