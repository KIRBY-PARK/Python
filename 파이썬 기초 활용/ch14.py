
numbers = [43, 21, 1, 8, 45, 12]

numbers.sort( )
print(numbers)

numbers.sort( reverse = True)
print(numbers)



'''
import random

def generate_lotto_numbers( ) :
    lotto_numbers = random.sample(range(1,46), 6)

    lotto_numbers.sort( )
    return lotto_numbers

print("생성된 로또 번호 : ", generate_lotto_numbers( ))
'''

'''
import random

a=[0, 0,0]

attempts = 0

while ((a[0] ==a[1] or a[0] ==a[2] or a[2] ==a[1]))  :
    a=[random.randint(0,9), random.randint(0,9),random.randint(0,9)]

print( str(a[0]) + str(a[1])+str(a[2])) #확인용 

while True :
    strike = 0
    ball = 0
    numberok = True
    isok = False

    while isok == False :
        b = input('서로 다른 3자리 숫자를 입력하세요.')

        if len(b) != 3 :
            print('3자리 숫자가 아닙니다.')
            numberok = False
            
        for i in range(3) :
            if(b[i]<'0' or b[i]>'9') :
                print('숫자가 아닙니다.')
                numberok = False
                

        if ((b[0] ==b[1] or b[0] ==b[2] or b[2] ==b[1]))  :
           print('서로 다른 3자리 숫자가 아닙니다. ')
           numberok = False
           
        if numberok == True :
            print(f'입력된 서로 다른 3자리 숫자는 {b}입니다. ')
            isok = True
            break

           
    for i in range(3) :
        if a[i] == int(b[i]) :
            strike = strike + 1

    for j in range(3) :
        for i in range(3) :
            if ( int(b[j]) == a[i] and i != j )  :
                ball = ball + 1

    attempts = attempts +1
        
    print(f" 스트라이크 {strike} 볼{ball}")

        
    if(strike ==3) :
        print("맞췄다. !")
        print(f"{ attempts}번 시도 만에 완성했습니다. ")
        break
      

        '''

              

            
    


'''
import random

a = [0,0,0]
strike = 0
ball = 0

while( a[0] == a[1] or a[0] == a[2] or a[2] == a[1]) :
    a = [random.randint(0,9), random.randint(0,9), random.randint(0,9)]

print( str(a[0]) + str(a[1]) + str(a[2]) )

b = input("서로 다른 3자리 숫자를 입력하세요.")

for j in range(3) :
    for i in range(3) :
        if ( int(b[j]) == a[i] and i != j) :
            ball = ball + 1
            break
        
print(f" 볼 {ball}")
'''
'''
import random

a = [0,0,0]
strike = 0

while( a[0] == a[1] or a[0] == a[2] or a[2] == a[1]) :
    a = [random.randint(0,9), random.randint(0,9), random.randint(0,9)]

print( str(a[0]) + str(a[1]) + str(a[2]) )

b = input("서로 다른 3자리 숫자를 입력하세요.")

for j in range(3) :

     

'''

'''
import random

a = [0,0,0]

while( a[0] == a[1] or a[0] == a[2] or a[2] == a[1]) :
    a = [random.randint(0,9), random.randint(0,9), random.randint(0,9)]

print( str(a[0]) + str(a[1]) + str(a[2]) )

while True :
    numberok = True
    isok = False

    while isok == False :
        b = input("서로 다른 3자리 숫자를 입력하세요.")

        if len(b) != 3 :
            print("3자리 숫자가 아닙니다.")
            numberok = False
            break

        for i in range(3) :
            if(b[i] < '0' or b[i] > '9') :
                print("숫자가 아닙니다. ")
                numberok = False
                break

        if( b[0] == b[1] or b[0] == b[2] or b[1] == b[2]) :
            print("서로 다른 3자리 숫자가 아닙니다.")
            numberok = False
            break

        if numberok == True :
            print(f' 입력된 서로 다른 3자리 숫자는  {b}입니다. ')
            isok = True            

'''


'''
numberok = False

while numberok == False :
    b = input(' 서로 다른 3자리 숫자를 입력하세요.')

    if ( b[0] == b[1] or b[0] == b[2] or b[1] == b[2]) :
        numberok = False

    else :
        print(f" 입력한 숫자는 {b}입니다.")
        number = True

        
    
'''
'''
numberok = False

while numberok == False :
    b = input(' 서로 다른 3자리 숫자를 입력하세요.')


    for i in range(3):
        if( b[i] < '0' or b[i] > '9' ) :
            print("숫자가 아닙니다.")
            numberok = False
            break
'''    

'''
isok = False

while isok == False :
    b = input(' 서로 다른 3자리 숫자를 입력하세요.')

    if len(b) != 3 :
        print('3자리 숫자가 아닙니다.')
    else :
        print(f"입력한 3자리 숫자 : {b}")
        isok = True
        
   '''     

'''

import random
a = [0,0,0]

while( a[0] == a[1] or a[0] == a[2] or a[1] == a[2] ) :
    a = [ random.randint(0,9),random.randint(0,9),random.randint(0,9)]

print( str(a[0]) + str(a[1]) + str(a[2]) )  # 확인용 

'''


'''
import random

for i in range(0,5) :
    a = [ random.randint(0,9),random.randint(0,9),random.randint(0,9)]

    print( str(a[0]) + str(a[1]) + str(a[2]) ) 
'''
