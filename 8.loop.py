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
embers3 = [
    {'name':'egoing', 'city':'seoul', 'job':'programmer'}, 
    {'name':'duru', 'city':'daegu', 'job':'dba'}
]
for member in members3:
    print(member['name'])