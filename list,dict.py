## 리스트와 딕셔너리
# 리스트 : 순서가 중요
# 딕셔너리 : key-value로 값을 담음

print('--------------------list--------------------')
a_list = ['사과',1,['한국','영국','일본']]
print(a_list[0])
print(a_list[2][1])

a_list.append(555) #추가
print(a_list[3])

result=a_list[-1] #맨 마지막께 나옴
print(result)

b_list = [1,4,7,21,32]
b_list.sort(reverse=True) #내림차순 정렬
print(b_list)

result = (5 in b_list) #리스트에 값이 있는지 확인 , 참 거짓으로 나옴
print(result)

print('--------------------dict--------------------')
a_dict = {'name':'bob','age':27,'friend':['영희','철수']}
result = a_dict['age']
print(result)
result = a_dict['friend'][1]
print(result)

a_dict['height'] = 180 #값 추가
print(a_dict)
print('height' in a_dict) #값이 있는지 확인

print('--------------------list+dict--------------------')
people = [
    {'name':'bob','age':27},
    {'name':'john','age':30},
    {'name':'joy','age':25}
]
print(people[1]['age'])
print(people[2]['name'])


people = [
{'name': 'bob', 'age': 20, 'score':{'math':90,'science':70}},
{'name': 'carry', 'age': 38, 'score':{'math':40,'science':72}},
{'name': 'smith', 'age': 28, 'score':{'math':80,'science':90}},
{'name': 'john', 'age': 34, 'score':{'math':75,'science':100}}
]

#smith의 science점수 출력하기
print(people[2]['score']['science'])