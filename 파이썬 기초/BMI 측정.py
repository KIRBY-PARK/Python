
print('키와 몸무게를 입력하세요')
h = float(input('키:'))
w = float(input('몸무게:'))

bmi = w/(h*h)*10000
print(bmi)

if bmi >= 25:
    print('비만')
else:
    print('정상')
