print('조건문---------------------')
money = 1000

if money>5000 :
    print('택시')
elif money>1500:
    print('버스')
else:
    print('걸어가자')

    print('들여쓰기하면 출력됨')


print('반복문---------------------')

fruits = ['사과','배','감','수박','딸기']

for fruit in fruits: #리스트에 있는 요소들을 출력
    print(fruit)

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
#나이가 20넘는 사람의 이름,나이 출력하기
for person in people:
    name = person['name']
    age = person['age']
    if age>20:
        print(name,age)

print('-----')
#enumerate 요소의 순서
for i,person in enumerate(people):
    name = person['name']
    age = person['age']
    print(i,name,age)
    if i>3: #i가 3이 넘으면 break, print가 먼저기 때문에 4까지 출력되고 멈춤
        break

print('연습문제---------')
num_list = [1, 2, 3, 6, 3, 2, 4, 5, 7, 2, 4]

#짝수 출력하기
for num in num_list:
    if(num%2==0):
        print(num)

#짝수 갯수 출력
count = 0
for num in num_list:
    if(num%2==0):
        count += 1
print("count=",count)

#리스트 안에 있는 모든 숫자 더하기
sum=0
for num in num_list:
    sum += num
print(sum)

#리스트 안에 있는 자연수 중 가장 큰 숫자 구하기
max = 0
for num in num_list:
    if(max<num):
        max=num
print(max)