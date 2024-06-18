###튜플
a=['사과','감','배']
a[1] = '수박'
print(a)
##리스트 - 불변형, 순서가 있음
a={'사과','감','배'}


###집합(set)
#중복제거 , 교집합/합집합/차집합 구할 수 있음
a=[1,2,3,5,4,8,7,5,6,8,4,9,1]
b=[3,2,1,0]

a_set = set(a)
b_set = set(b)
#교집합
print(a_set & b_set)
#합집합
print(a_set | b_set)
#차집합
print(a_set - b_set)


###f-string
#문자열을 표현할 때 편하게 쓸 수 있음 f+문자
scores = [
    {'name':'영수','score':70},
    {'name':'영희','score':65},
    {'name':'기찬','score':75},
    {'name':'희수','score':23},
    {'name':'서경','score':99},
    {'name':'미주','score':100},
    {'name':'병태','score':32}
]

for s in scores:
    name = s['name']
    score = str(s['score'])
    #scroe는 숫자, 문자로 바꿔줘야함
    print(name+'의 점수는'+score+'점입니다.')
    print(f'{name}의 점수는 {score}점입니다.')


### 예외처리 try-except

people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby'},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

for person in people:
    try:
        if person['age'] >20:
            print(person['name'])
    except:
        print('에러입니다.')
    #에러난 곳은 "에러입니다."문구 나오고 멈추지 않고 계속 돌아감

