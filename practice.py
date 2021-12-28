print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))
print('풍선')
print("나비")
print("ㅋ"*9) #개쩌네;;;
print(5>10)
print(5<10)
print(not True)
print(not False)
print(not (5>10))
# 애완동물 소개해봐
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집"+ animal +"의 이름은 " + name + "에요")
hobby = "공놀이"
#print(name +"는 " + str(age) +"살이며, "+ hobby +"을 아주 좋아해요")
print(name,"는 ", age,"살이며, ", hobby ,"을 아주 좋아해요")
print("연탄이는 어른일까요? " + str(is_adult))

station = "사당"
print(station+" 행 열차가 들어오고 있습니다.")
station = "신도림"
print(station+" 행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station+" 행 열차가 들어오고 있습니다.")

print(2**3)#2^3 = 8
print(5%3)#5 / 3 의 나머지 2 출력
print(5//3)# 5/3 의 몫 1이 나옴
print(10//3)# 5/3 의 몫 3이 나옴

print(1 != 3)
print(not( 1 != 3))

print((3 >0 and (3 < 5))) # True
print((3 > 0) & (3 <5 )) # True

print((3 > 0) or (3 > 5)) # True
print((3 > 0) | (3 > 5)) # True

print(5 > 4 > 3)#True
print(5 > 7 > 1)#False

number = 2 + 3 * 4
print(number)
number = number + 2
print(number)
number += 2
print(number)
number *= 2
print(number)
number /= 2
print(number)
number -= 2
print(number)


print(abs(-5)) # 5 abs는 absolute다. 절대값
print(pow(4,2)) # 4^2 = 4*4 = 16
print(max(5, 12)) # 12 최대값 반환
print(min(5, 12)) # 5 최소값 반환
print(round(3.14)) # 3 반올림
print(round(4.99)) # 5

from math import *
print(floor(4.99)) # 내림 4
print(ceil(3.14)) # 올림 4
print(sqrt(16)) # 제곱근 4

from random import *
print(random()) # 0.0 이상 ~ 1.0 미만 난수 생성
print(random() * 10) # 0.0이상 ~ 10.0 미만 난수 생성
print(int(random()*10)) # 0이상 ~ 10미만 난수 생성
print(int(random() * 10)+1) # 1이상 ~ 10이하 난수 생성

print(int(random()*45)+1) # 1이상 ~ 45이하 난수 생성
print(randrange(1, 46)) # 1이상 ~ 46미만 난수 생성

print(randint(1, 45))  # 1이상 ~ 45 이하 난수 생성

sentence = '나는 소년입니다.'
print(sentence)
sentence2 = "파이썬은 쉬워요."
print(sentence2)
sentence3 = """
나는 소년이고 파이썬은 쉬워요
"""
print(sentence3)

#슬라이싱
jumin = "990120-1234567"

print("성별 : " + jumin[7]) #슬라이싱 이용
print("연 : " + jumin[0:2]) # 0부터 2미만(직전)까지
print("월 : " + jumin[2:4]) # 2부터 4미만(직전)까지
print("일 : " +jumin[4:6]) #
print("생년월일 :" + jumin[:6]) # 처음부터 6미만(직전)까지
print("뒤 7자리 : " + jumin[7:]) #7부터 끝까지
print("뒤 7자리(뒤에서부터) :" + jumin[-7:])#맨 뒤는 -1부터 시작 == 맨 뒤에서 7번째 끝까지


python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))

print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1) # n 차고 다음 n은 어딨나
print(index)

print(python.find("n")) # 값이 없으면 -1로 반환
print(python.find("java"))
#print(python.index("Java")) # 값이 없으면 오류 처리

print(python.count("n"))

print("a" + "b")
print("a", "b")

print("나는 %d살입니다." % 20) # 정수로 받기
print("나는 %s을 좋아해요." %"파이썬") #문자열로 반기
print("Apple은 %c로 시작해요" %"A") #문자로 받기
print("나는 %s색과 %s색을 좋아해요" %("파란", "빨간"))

print("나는 {}살 입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요" .format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요" .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요" .format("파란", "빨간"))

print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color = "빨간"))

#파이썬 3.6이상
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")

#탈출문자
print("백문이 불여일견\n백견이 불여일타")

print("저는 ""나도코딩"" 입니다.")
print("저는 '나도코딩' 입니다.")
print('저는 "나도코딩" 입니다.')
print("저는 \"나도코딩\" 입니다.")

print("나나나나\\나나나나\\나나나나")
print("Red Apple\rPine")
print("Redd\bApple")

print("Red\tApple")

#리스트

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

print(subway.index("조세호"))

subway.append("하하")
print(subway)

subway.insert(1,"정형돈")
print(subway)

print(subway.pop()) #뒤에서부터 제거
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

subway.append("유재석") #뒤에다 넣기
print(subway)
print(subway.count("유재석"))

num_list = [5,4,3,2,1]
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

num_list.clear()
print(num_list)

num_list = [5,2,4,3,1]
mix_list = ["조세호", 20, True]

num_list.extend(mix_list)
print(num_list)

#사전(dictionary)

cabinet = {3:"유재석", 100:"김태호"} #key 3, value 유재석 key100, value 김태호
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
#print(cabinet[5]) 오류 발생되어 종료
print(cabinet.get(5)) #None 으로 나옴
print(cabinet.get(5, "사용가능")) #없으면 뒤 값을 사용
print("hi")

print(3 in cabinet) # True or False
print(5 in cabinet) # True or False

cabinet = {"a-3":"유재석", "a-100":"김태호"}
print(cabinet["a-3"])
print(cabinet["a-100"])

print(cabinet)
cabinet["a-3"] = "김종국" # value 바꾸기 가능
cabinet["c-20"] = "조세호"
print(cabinet)

del cabinet["a-3"]
print(cabinet)

print(cabinet.keys()) # 키값만 
print(cabinet.values()) # 밸류값만
print(cabinet.items()) # 전부다

cabinet.clear()
print(cabinet)

#튜플-변경불가(배열..?) 리스트보다 속도가 빠름
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("유재석" , 30, "코오딩")
print(name, age, hobby)

#집합(set) 중복 X, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

print(java & python) #교집합
print(java.intersection(python))#교집합

print(java | python) #합집합
print(java.union(python)) #합집합

print(java - python) #차집합
print(java.difference(python)) #차집합

python.add("김태호")
print(python)

java.remove("김태호")
print(java)

#자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

#조건문(if)

# weather = "맑아요"
# #if 조건: 실행명령문
# if weather == "비" : print("우산을 챙기세요")
# elif weather == "미세먼지" : print("마스크를 챙기세요")
# else : print("준비물 필요 없어요")

# weather = input("오늘 날씨는 어때요? ")
# if weather == "비" or weather == "눈": print("우산을 챙기세요")
# elif weather == "미세먼지" : print("마스크를 챙기세요")
# else : print("준비물 필요 없어요")

# temp = int(input("기온은 어때요?"))
# if 30 <= temp :
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp < 30 :
#     print("괜찮은")
# elif 0 <= temp < 10 :
#     print("외투를 챙기세요")
# else : print("너무 추워요. 나가지마세요")

#반복문(for)

for waiting_no in[0,1,2,3,4]:
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(5): #0,1,2,3,4
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(1,6): #1,2,3,4,5
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]

for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))


#반복문(while)

customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피가 폐기처분되었습니다.")
''''
무한루프
customer = "아이언맨"
index = 1
while True :
    print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(customer, index))
    index += 1
'''

# customer = "토르"     한글키가 인풋에서 잘 안먹음
# person = "Unknown"
# while person !=customer :
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")

#Continue 와 Break

absent = [2, 5] #결석
no_book = [7] #책을 깜빡했음
for student in range(1, 11): #1,2,3,4,5,6,7,8,9,10
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지 {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))

#한줄 for
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]

students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)

#함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")


def deposit(balance, money):
    print("입금이 완료 되었습니다. 잔액은 {0} 원 입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money) : #출금
    if balance >= money: #잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance+money))
        return balance + money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance

def withdraw_night(balance, money): #저녁에 출금
    commission = 100 #수수료 100원
    return commission, balance - money - commission

balance = 0 # 잔액
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000)
print(balance)
balance = withdraw(balance, 500)
print(balance)
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이며 잔액은{1}원 입니다".format(commission, balance))

#기본값
def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
        .format(name, age, main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

def profile2(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
        .format(name, age, main_lang))

profile2("유재석")
profile2("김태호")

#키워드값
def profile3(name, age, main_lang):
    print(name, age, main_lang)

profile3(name="유재석", main_lang="파이썬", age=20)
profile3(main_lang="파이썬", age=25, name="김태호")

#가변인자
def profile3(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end =" ")
    print()

profile3("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile3("김태호", 25, "Kotlin", "Swift")

#지역변수 전역변수
gun = 10

def checkpoint(soldiers): # 경계근무
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2)
print("남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))

