

import random

game =  5
win = 0
even = 0
lose = 0

options = ["가위", "바위", "보"]

def get_computer_choice( ) :
    return random.choice(options)

def get_user_choice( ) :
    user_input = input("가위, 바위, 보 중 하나를 선택하세요. ")

    while user_input not in options :
        user_input = input("잘못된 입력입니다. 가위, 바위, 보 중 하나를 정확히 선택하세요. ")

    return  user_input

def determine_winner( user_choice,  computer_choice) :
    global win
    global lose
    global even
    
    if user_choice == computer_choice :
        even = even + 1
        print("무승부 입니다. ")

    elif ( user_choice == "가위" and computer_choice == "보") or \
          ( user_choice == "바위" and computer_choice == "가위") or \
          ( user_choice == "보" and computer_choice == "바위")  :
        print("축하합니다. 당신이 이겼습니다.")
        win = win + 1

    else :
        print("아쉽지만, 컴퓨터가 이겼습니다. ")
        lose = lose + 1

def play_game( ) :
    computer_choice = get_computer_choice( ) 
    user_choice = get_user_choice( )
    
    print(f"당신의 선택 : {user_choice}")
    print(f"컴퓨터의 선택 : {computer_choice}")

    determine_winner( user_choice,  computer_choice)
    print(f"{win}승 {even}무 {lose}패입니다. ")
    
while(win <3 and lose < 3) :    
#while(not (win >=3 or lose >= 3)) :
    play_game( )    
    game = game - 1

'''
import random

game =  5
win = 0
even = 0
lose = 0

options = ["가위", "바위", "보"]

def get_computer_choice( ) :
    return random.choice(options)

def get_user_choice( ) :
    user_input = input("가위, 바위, 보 중 하나를 선택하세요. ")

    while user_input not in options :
        user_input = input("잘못된 입력입니다. 가위, 바위, 보 중 하나를 정확히 선택하세요. ")

    return  user_input

def determine_winner( user_choice,  computer_choice) :
    global win
    global lose
    global even
    
    if user_choice == computer_choice :
        even = even + 1
        print("무승부 입니다. ")

    elif ( user_choice == "가위" and computer_choice == "보") or \
          ( user_choice == "바위" and computer_choice == "가위") or \
          ( user_choice == "보" and computer_choice == "바위")  :
        print("축하합니다. 당신이 이겼습니다.")
        win = win + 1

    else :
        print("아쉽지만, 컴퓨터가 이겼습니다. ")
        lose = lose + 1

def play_game( ) :
    computer_choice = get_computer_choice( ) 
    user_choice = get_user_choice( )
    
    print(f"당신의 선택 : {user_choice}")
    print(f"컴퓨터의 선택 : {computer_choice}")

    determine_winner( user_choice,  computer_choice)
    print(f"{win}승 {even}무 {lose}패입니다. ")
    
    
while(game) :
    play_game( )    
    game = game - 1
'''

'''
import random

game =  3

options = ["가위", "바위", "보"]

def get_computer_choice( ) :
    return random.choice(options)

def get_user_choice( ) :
    user_input = input("가위, 바위, 보 중 하나를 선택하세요. ")

    while user_input not in options :
        user_input = input("잘못된 입력입니다. 가위, 바위, 보 중 하나를 정확히 선택하세요. ")

    return  user_input

def determine_winner( user_choice,  computer_choice) :
    if user_choice == computer_choice :
        print("무승부 입니다. ")

    elif ( user_choice == "가위" and computer_choice == "보") or \
          ( user_choice == "바위" and computer_choice == "가위") or \
          ( user_choice == "보" and computer_choice == "바위")  :
        print("축하합니다. 당신이 이겼습니다.")

    else :
        print("아쉽지만, 컴퓨터가 이겼습니다. ")

def play_game( ) :
    computer_choice = get_computer_choice( ) 
    user_choice = get_user_choice( )
    
    print(f"당신의 선택 : {user_choice}")
    print(f"컴퓨터의 선택 : {computer_choice}")

    determine_winner( user_choice,  computer_choice)
    
    
while(game) :
    play_game( )    
    game = game - 1
'''

'''
import random

game =  3

options = ["가위", "바위", "보"]

def get_computer_choice( ) :
    return random.choice(options)

def get_user_choice( ) :
    user_input = input("가위, 바위, 보 중 하나를 선택하세요. ")

    while user_input not in options :
        user_input = input("잘못된 입력입니다. 가위, 바위, 보 중 하나를 정확히 선택하세요. ")

    return  user_input

def determine_winner( user_choice,  computer_choice) :
    if user_choice == computer_choice :
        print("무승부 입니다. ")

    elif ( user_choice == "가위" and computer_choice == "보") or \
          ( user_choice == "바위" and computer_choice == "가위") or \
          ( user_choice == "보" and computer_choice == "바위")  :
        print("축하합니다. 당신이 이겼습니다.")

    else :
        print("아쉽지만, 컴퓨터가 이겼습니다. ")

    
while(game) :
    computer_choice = get_computer_choice( ) 
    user_choice = get_user_choice( )
    
    print(f"당신의 선택 : {user_choice}")
    print(f"컴퓨터의 선택 : {computer_choice}")

    determine_winner( user_choice,  computer_choice)
    
    
    game = game - 1

'''

'''
import random

game =  3

options = ["가위", "바위", "보"]

def get_computer_choice( ) :
    return random.choice(options)

def get_user_choice( ) :
    user_input = input("가위, 바위, 보 중 하나를 선택하세요. ")

    while user_input not in options :
        user_input = input("잘못된 입력입니다. 가위, 바위, 보 중 하나를 정확히 선택하세요. ")

    return  user_input

   
while(game) :
    computer_choice = get_computer_choice( ) 
    user_choice = get_user_choice( )
    
    print(f"당신의 선택 : {user_choice}")
    print(f"컴퓨터의 선택 : {computer_choice}")

    if user_choice == computer_choice :
        print("무승부 입니다. ")

    elif ( user_choice == "가위" and computer_choice == "보") or \
          ( user_choice == "바위" and computer_choice == "가위") or \
          ( user_choice == "보" and computer_choice == "바위")  :
        print("축하합니다. 당신이 이겼습니다.")

    else :
        print("아쉽지만, 컴퓨터가 이겼습니다. ")
    
    game = game - 1

'''

'''
import random

game =  5

options = ["가위", "바위", "보"]

def get_computer_choice( ) :
    return random.choice(options)

def get_user_choice( ) :
    user_input = input("가위, 바위, 보 중 하나를 선택하세요. ")

    while user_input not in options :
        user_input = input("잘못된 입력입니다. 가위, 바위, 보 중 하나를 정확히 선택하세요. ")

    return  user_input
    
while(game) :
    user_choice = get_user_choice( )
    
    print(f"당신의 선택 : {user_choice}")
    
    game = game - 1
'''
'''
import random

game =  5

options = ["가위", "바위", "보"]

def get_computer_choice( ) :
    return random.choice(options)

while(game) :
    computer_choice = get_computer_choice( )
    
    print(f"컴퓨터의 선택 : {computer_choice}")
    
    game = game - 1
'''
'''
import random

game =  5

while(game) :
    options = ["가위", "바위", "보"]

    print(f"컴퓨터의 선택 : {options[0]}")
    print(f"컴퓨터의 선택 : {options[1]}")
    print(f"컴퓨터의 선택 : {options[2]}")

    game = game - 1

'''
'''
import random

game =  5

while(game) :
    options = ["가위", "바위", "보"]

    computer_choice = random.choice(options)

    print(f"컴퓨터의 선택 : {computer_choice}")

    game = game - 1
'''
