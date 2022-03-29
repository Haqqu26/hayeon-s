## 6.Boolean
print(True)
print(False)
 #비교연산자(연산의결과 Boolean이 되는 연산자)
print(1 == 1)
print(1 == 2)
print(1 > 2)

## 7.Conditional 조건문
print(1)
if False:
    print(2)
    print(3)
print(4)

print(1)
if True:
     print(2.1)
     print(3.1)
else:
     print(2.2)
     print(3.2)
print(4)

input_id = input('아이디를 입력해주세요. ')
input_pwd = input('비밀번호를 입력해주세요. ')
if input_id == 'yeon' :
    if input_pwd == '0000' :
        print('안녕하세요')
    else:
        print('비밀번호가 다릅니다.')
else:
    print('아이디가 다릅니다.')

## 8.Loop
 # 배열안에 문자열
members = ['ayla', 'ella']
for member in members:
    print('name :',member)
 # 큰 배열 안에 작은 배열, 작은 배열 안에 문자열
members2 = [
    ['ayla', 'daegu', 'programmer'],
    ['ella', 'seoul', 'forwarder']
]
print(members2[0][0])
for member in members2:
    print(member[0], member[1])

ayla1 = ['ayla', 'daegu', 'programmer'] #리스트:성격이 같은 데이터를 그룹핑, 순서가 있다
ayla2 = {'name': 'ayla', 'city': 'daegu', 'job':'programmer'} #사전형 각각의 원소는 이름을 가지며 성격이 다르다
print(ayla2['city'])
for name in ayla2:
    print(ayla2[name])

## 9.Function
def sum(left,right):
    return left+right
print(sum(10,20))
