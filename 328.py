## 1.program
print(1)
print(2)
print(3)


## 2.datatype
 # Number
print(1)
print(1.1)
print(1+1)
print(2-1)
print(2*2)
print(6/2)
print(pow(3,2))
import random
print(random.random())
 
 # String
print('Hello')
print("Hello")
print("""
Hello
World
 """)
print(len('Hello'))
print('Hell World'.replace('Hell','Hello'))

 # List(리스트:연관된 데이터를 그룹핑하여 이름 붙인 것)
member = ['ayla','ella']
print(member[0])
print(len(member))
import random
print(random.choice(member))

score = [100,200,300]
print(sum(score))


## 3.Variable(변수:데이터에 이름을 붙인 것)
가격 = 10000
부가세율 = 0.1
결과 = 가격*부가세율
print(결과)

name = 'ayla'
print('안녕하세요. '+name+'님, ...today... '+name+'님 좋은 하루 보내세요.')
print(f'안녕하세요. {name}님, ...today... {name}님 좋은 하루 보내세요.')


## 4.input 명령어환경에서 입력값을 프로그램으로 가져오는 수단
가격 = float(input('가격? '))
부가세율 = 0.1
부가세 = 가격 * 부가세율
print(부가세)