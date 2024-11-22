
import random

m_ball = 3
w_ball = 3
y_ball = 3

while( not (m_ball == 0 or w_ball == 0 or y_ball == 0)) :
    m_robot = random.randint(1,3)
    w_robot = random.randint(1,3)
    print(f"여자 봇은 {w_robot}을 선택했습니다. ")
    print("당신의 선택은 ??? ")
    you = int(input("1.나머지가 1이다. 2. 나머지가 2이다. 3. 나머지가 0이다."))

    while( w_robot == you) :
        print("당신과 여자 봇이 같은 것을 선택했습니다. ")
        print(f"여자 봇은 {w_robot}을 선택했습니다. ")
        print("당신의 선택은 ??? ")
        you = int(input("1.나머지가 1이다. 2. 나머지가 2이다. 3. 나머지가 0이다."))

    if(m_robot == you) :
        print("당신이 이겼습니다. ")
        y_ball = y_ball + 1
        m_ball = m_ball - 1

    elif(m_robot == w_robot) :
        print("여자 봇이 이겼습니다. ")
        w_ball = w_ball + 1
        m_ball = m_ball - 1

    else :
        print("남자 봇이 이겼습니다. ")
        m_ball = m_ball + 2
        w_ball = w_ball - 1
        y_ball = y_ball - 1

    print(f"남자 봇 선택 : {m_robot}, 여자 봇 선택 : {w_robot} 당신 선택 : {you }입니다. ")
    print(f"남은 볼은 남자 봇 : {m_ball}개, 여자 봇 : {w_ball}개 , 당신 : {y_ball}개 입니다. ")
    print("                                ")   

'''
import random

m_ball = 3
w_ball = 3
y_ball = 3

while( not (m_ball == 0 or w_ball == 0 or y_ball == 0)) :
    m_robot = random.randint(1,3)
    w_robot = random.randint(1,3)
    print(f"여자 봇은 {w_robot}을 선택했습니다. ")
    print("당신의 선택은 ??? ")
    you = int(input("1.나머지가 1이다. 2. 나머지가 2이다. 3. 나머지가 0이다."))

    if(m_robot == you) :
        print("당신이 이겼습니다. ")
        y_ball = y_ball + 1
        m_ball = m_ball - 1

    elif(m_robot == w_robot) :
        print("여자 봇이 이겼습니다. ")
        w_ball = w_ball + 1
        m_ball = m_ball - 1

    else :
        print("남자 봇이 이겼습니다. ")
        m_ball = m_ball + 2
        w_ball = w_ball - 1
        y_ball = y_ball - 1

    print(f"남자 봇 선택 : {m_robot}, 여자 봇 선택 : {w_robot} 당신 선택 : {you }입니다. ")
    print(f"남은 볼은 남자 봇 : {m_ball}개, 여자 봇 : {w_ball}개 , 당신 : {y_ball}개 입니다. ")
    print("                                ")    
'''

'''
print("메뉴를 선택하세요.")

number = int(input("1.콜라  2.사이다  3. 환타 "))

if(number == 1) :
             print("콜라를 선택하셨습니다. ")
elif(number == 2) :
             print("사이다를 선택하셨습니다. ")
elif(number == 3) :
             print("환타를 선택하셨습니다. ")
else :
    print("잘 못 누르셨습니다. ")
'''

'''
sum = 0
number = int(input("1부터 더하고 싶은 양의 정수를 입력하세요."))
for i in range(1,number+1) :
    sum = sum + i
print(f"1부터 {i}까지 더한 결과 : {sum}")
'''
'''
sum = 0
number = int(input("1부터 더하고 싶은 양의 정수를 입력하세요."))
for i in range(1,number+1) :
    sum = sum + i
    print(f"1부터 {i}까지 더한 결과 : {sum}")
'''
    
'''

'''
'''
sum = 0

for i in range(1,11) :
    sum = sum + i
    print(f"1부터 {i}까지 더한 결과 : {sum}")

'''

'''
for i in range(0,3) :
    print(f"{i} 푸쉬 업 ")

print(f"{i} 푸쉬 다운 ")
'''


'''
for i in range(1,4) :
    print(f"{i} 푸쉬 업 ")
    print(f"{i} 푸쉬 다운 ")
'''
'''
a = 3
b = 5

while( not(a==10 or b==10)) :
       print(f"a = {a}  b={b}")
       a = a+1
       b = b+1

'''
'''
a = 3
b = 5

print(f"a == 5 and b==5의 결과는 {a == 5 and b==5}")
print(f"a == 5 or b==5의 결과는 {a == 5 or b==5}")
print(f"not(a == 5 or b==5)의 결과는 {not(a == 5 or b==5)}")


'''
a=1
b=0
'''
print(f"a and b = {a and b }")
print(f"a or b = {a or b }")
print(f" not a = {not a }")
'''
