#map, filter, lambda

### map - 리스트의 모든 원소 조작

people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby', 'age': 57},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

# def check_adult(person):
#     if person['age']>20:
#         return '성인'
#     else:
#         return '청소년'

#if문 한줄로 작성하기
def check_adult(person):
    return ('성인' if person['age'] >20 else '청소년')

# people을 하나하나 돌면서 check_adult 함수에 넣어라.
result = map(check_adult,people)

#print(result) <- 그냥 map인 상태, list를 붙여줘서 결과값을 list로 넣어줌
print(list(result))

#한줄로 작성하기
#result = map(lambda x:x, people) #people을 돌면서 x에 넣는 것
#result = map(lambda person:person, people)
result = map(lambda person:('성인' if person['age'] >20 else '청소년'), people)  #people을 돌면서  person에 넣고 그 prson을 '성인 ~~~' 로 return 해라.



### filter - 리스트의 모든 원소 중 특별한 것만 뽑기 (True인것만 뽑음)
# lambda에 'x'를 많이 씀 (관용적)
result = filter(lambda x:x['age']>20, people)
print('filter result = ')
print(list(result))