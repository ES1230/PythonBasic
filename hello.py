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

