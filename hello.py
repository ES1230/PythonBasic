print('hello python')

# 기본계산
print("--------------------")
a=3
b=2
print("a=",a," b=",b)
print("a+b=",a+b)
print("a/b=",a/b)
print("a%b=",a%b)
print("a**b=",a**b) #a의 b제곱

c = (3==2)
print(c)

#문자열
print("--------------------")
first_name = 'eunseon'
last_name = 'ryu'

print(first_name+last_name)

a='2'
b=str(2)
print(a+b)

text='abcdefghi'
result1 = text[3:] #3번째부터 쭉
result2 = text[:3]  #0번부터 3번까지 나빼고
result3 = text[3:7]  #3번부터 7번까지 나빼고
print(result1)
print(result2)
print(result3)

email = 'abc@naver.com'
result = email.split('@') #@로 분리되어 0, 1번째가 됨
print(result)
result = email.split('@')[1].split('.') # @로 분리된 문자열 중 1번째꺼를 .으로 분리
print(result)

#지역번호 뽑아보기
a='02-1234-1234'
text=a.split('-')[0]
print(text)
print("--------------------")

#함수
def sum(a,b):
    print('a랑 b를 더합니다')
    return a+b

result = sum(1,2)
print(result)

def bus_rate(age):
    if age>65:
        print('무료입니다')
    elif age>20:
        print('성인입니다')
    else:
        print('청소년입니다')

bus_rate(50)

#성별 추출하기
def check_gender(pin):
    if (pin[7]=='1' or pin[7]=='3'):
        print('남성입니다')
    else:
        print('여성입니다')

check_gender('000101-1012345')
check_gender('000101-2012345')
check_gender('000101-4012345')

#성별추출 다른방법
def check_gender(pin):
    num = pin.split('-')[1][:1]
    if int(num)%2!=0:
        print('남성입니다')
    else:
        print('여성입니다')

check_gender('000101-1012345')
check_gender('000101-2012345')
check_gender('000101-4012345')


##한줄 연습, if문 짧게 쓰기
num=3

# if num % 2 == 0:
#     result='짝수'
# else:
#     result='홀수'

result=('짝수' if num % 2== 0 else '홀수')
print(f'{num}은 {result}입니다')

a_list = [1,3,2,5,1,2]
#[2,6,4,10,2,4] 이렇게 만들기

b_list = []
# for a in a_list:
#     b_list.append(a*2)

b_list = [a*2 for a in a_list]

print(b_list)


###함수 심화
## 여러개의 인수를 하나의 매개변수르 받을 때 관례적으로 args라는 이름을 사용 (arguments)
def cal(*args):
    for name in args:
        print(f'{name}야 밥먹어라')
        
cal('영수','철수','영희')

## **kwargs
# 키워드 인수를 여러 개 받는 방법
# dictionary형태로 저장됨
def cal2(**kwargs):
    print(kwargs)

cal2(name='bob',age='30',height=180) 


###클래스
class Monster():
    hp = 100
    alive = True

    def damage(self,attack):
        self.hp = self.hp-attack
        if self.hp <0:
            self.alive = False

    def status_check(self):
        if self.alive == True:
            print('살았다')
        else:
            print('죽었다')


m1 = Monster()
m1.damage(150)
m1.status_check()

m2 = Monster()
m2.damage(90)
m2.status_check()