
while(True) :
    momey_temp = input("환전할 금액을 입력하세요.")

    if( not momey_temp.isnumeric( )) :
        print("정수가 아닙니다. 다시 입력하세요.")
        continue

    money = int(momey_temp)
    print(f"환전할 금액은 {money}입니다. ")

    break 
    
while(True) :
    dollar_temp = input("환률을 입력하세요.")

    if( not dollar_temp.isnumeric( )) :
        print("정수가 아닙니다. 다시 입력하세요.")
        continue

    dollar = int(dollar_temp)
    print(f"1달라 환율은 {dollar}입니다. ")

    break

dollar_100 = money//(dollar*100)
dollar_10= (money%(dollar*100))// (dollar*10)
dollar_5= (money%(dollar*10))// (dollar*5)
dollar_1= (money%(dollar*5))// (dollar)
money_return = money%(dollar)

print(f"백달러 지폐는 {dollar_100}장 입니다. ")
print(f"십달러 지폐는 {dollar_10}장 입니다. ")
print(f"오달러 지폐는 {dollar_5}장 입니다. ")
print(f"일달러 지폐는 {dollar_1}장 입니다. ")
print(f"돌려받을 한화는 {money_return}원 입니다. ")

'''
import random
red = 0
sum = 0
game = 1

while(game) :
    input("게임을 하려면 엔터를 치세요.")
    red = random.randint(1,6)
    sum = sum + red

    print(f"red는 {red}이고 합은 {sum}입니다. ")

    if(sum%5 == 0 or sum%7 == 0) :
        print("아악...폭탄이다. ")
        game = 0

    if(sum > 20) :
        print("미션 성공 !!! ")
        break

'''


















'''
import random
sum = 0
game = 1

while(game) :
    input("게임을 하려면 엔터를 치세요.")
    red = random.randint(1,6)
    sum = sum + red
    print(f"red는 {red}이고 합은 {sum}입니다. ")

    if(sum % 3 ==0) :
        print("아악....폭탄이다.")
        game = 0

    if(sum >18) :
        print("미션 성공 !!!")
        break 
    '''
'''
import random

game = 3

while(game) :
    input("게임을 하려면 엔터를 치세요.")
    red = random.randint(1,6)
    blue = random.randint(1,6)
    sum = red + blue
    print(f" red는 {red} blue는 {blue}합은 {sum}입니다. ")

    if(sum > 9) :
        print("백만 장자가 되었네요...")
        break
    else :
        print("거지가 될 것 같아요..슬퍼요.")

    game = game-1
    print(f"기회는 {game}번 남았어요 ..")

    if(game == 0) :
        print("아악....거지가 되었어요..")
'''

'''
import random

game = 10

number = random.randint(1,50)

while(game) :
    minsu = int(input("1부터 50까지 정수를 입력하세요."))

    if(number > minsu) :
        print("컴이 너보다 커")
    elif(number< minsu) :
        print("네가 컴보다 커")
    else :
        print("미션 완료 !!! 미숙 구출 완료")
        break

    game = game-1
    print(f"{game}번 남았쓰...")
    if(game ==0) :
        print("게임 오버 !!! 멍청한 놈...ㅎㅎㅎ ")
        break

'''
'''
import random

game = 5

number = random.randint(1,10)

while(game) :
    minsu = int(input("1부터 10까지 정수를 입력하세요."))

    if(number > minsu) :
        print("컴이 너보다 커")
    elif(number< minsu) :
        print("네가 컴보다 커")
    else :
        print("미션 완료 !!! 미숙 구출 완료")
        break

    game = game-1
    print(f"{game}번 남았쓰...")
    if(game ==0) :
        print("게임 오버 !!! 멍청한 놈...ㅎㅎㅎ ")
        break


    '''
    
'''
import random

game = 5

while(game) :
    number = random.randint(1,10)
    print(f"생성된 랜덤 정수 {number}")
    game = game-1
'''
