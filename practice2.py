#표준 입출력
print("Python", "Java", sep=",") # ,에 ,를 넣어준다. 안넣어주면 white space(띄어쓰기)가 들어간다.
print("Python", "Java", "JavaScript", sep=" vs ") # ,에 vs를 넣어준다. 안넣어주면 white space(띄어쓰기)가 들어간다.
print("Python", "Java", sep=",", end=" ") #end 다음에는 이어서 출력이 된다.
print("무엇이 더 재미있을까요?")

# import sys
# print(print("Python", "Java", file=sys.stdout) # 표준출력이 문장이 찍힌다
# print(print("Python", "Java", file=sys.stderr) # 에러처리가 된다. 공부 더 필요

# scores = {"수학" : 0, "영어":50, "코딩":100}
# for subject, scroe in scores.items():
#     #print(subject,scroe)
#     print(subject.ljust(8),str(scroe).rjust(3), sep=":") #8칸 확보 후 왼쪽정렬, 3칸 확보 후 오른쪽 정렬

# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3)) # zfill 은 0으로 채워지는데 3개공간을 확보하는데 값이 없으면 0으로 채우란 뜻이다.


# answer = input("아무 값이나 입력하세요 : ")
# print("입력한 값은 "+answer+"입니다.")  # input은 항상 str로 받아준다. 숫자를 넣어줘도 int가 아닌 str이라는 것이다.

#다양한 출력 포맷

##빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500)) # >는 오른쪽. >전에 한칸을 띄웠다 500까지 합쳐서 10공간을 확보한 것

##양수일 땐 +로 표신, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

##왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<10}".format(500))

##3자리 마다 콤마를 찍어주기
print("{0:,}".format(100000000000))

##3자리 마다 콤마를 찍어주기, +-부호도 붙이기
print("{0:+,}".format(100000000000))
print("{0:+,}".format(-100000000000))

##3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
##돈이 많으면 행복하니깐 빈 자리는 ^ 로 채워주기
print("{0:^<+30,}".format(100000000))

##소수점 출력
print("{0:f}".format(5/3))
##소수점 특정 자리수까지만 표시(소수정 3째 자리에서 반올림)
print("{0:.2f}".format(5/3))

#파일 입출력
# score_file = open("scroe.txt", "w", encoding="utf8") # w는 write
# print("수학 : 0", file=score_file) #파일 생성됨
# print("수학 : 50", file=score_file)
#score_file.close()

# score_file = open("scroe.txt", "a", encoding="utf8") # a는 append
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 80")
# score_file.close()

score_file = open("scroe.txt", "r", encoding="utf8") # r는 read
print(score_file.read())
score_file.close() 

score_file = open("scroe.txt", "r", encoding="utf8")
print(score_file.readline()) # 줄별로 일기, 한 줄 일고 커서는 다음 줄로 이동(줄바꿈)
print(score_file.readline(), end="") #자동개행을 하지않으려면 바로 이어서 출력을 이용
print(score_file.readline(), end="")
score_file.close()

score_file = open("scroe.txt", "r", encoding="utf8")
while True:     #while을 이용해서 전부다 읽어오기
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()

score_file = open("scroe.txt", "r", encoding="utf8")
lines = score_file.readlines() #list 형태로 저장
for line in lines:
    print(line, end="")

score_file.close()

#pickle <프로그램상에서 사용하고 있는 데이터를 파일형태로 저장

# import pickle
# profile_file = open("profile.pickle", "wb") # wb는 Write  Binary
# profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb") # wb는 Read  Binary
# profile = pickle.load(profile_file) # file에 있는 정보를 porfile에 불러오기
# print(profile)
# profile_file.close()

#with <피클도 가능하다. 우선 import 로 pickle모듈 불러온 다음에 / 매번 클로즈를 해줄 필요 없다.

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요.")

with open("study.txt","r",encoding="utf8") as study_file:
    print(study_file.read())

#클래스

# #마린 : 공격 유닛, 군인, 총을 쏠 수 있음
# name = "마린" #유닛 이름
# hp = 40 # 유닛의 체력
# damage = 5 # 유닛의 공격력

# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# # 탱크 : 공격 유닛, 탱크, 포를 쏠 수 있는데, 일반모드 / 시즈모드.
# tank_name = "탱크" #유닛 이름
# tank_hp = 150 # 유닛의 체력
# tank_damage = 35 # 유닛의 공격력

# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)

#탱크가 2개 이상일 때? 클래스를 이용하자 붕어빵 틀이라고 생각하자.

# class Unit :
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

#__init__
# 클래스로부터 만들어지는 것  = 객체
# 마린과 탱크는 객체
# 마린과 탱크는 Unit의 인스턴스

# 멤버변수
# self.name, self.hp 등에서 name과 hp가 멤버 변수if wraith1.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith1.name))
# 레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인트 컨트롤 : 상대방 유닛을 내 것으로 만드는 것(빼앗음)
# wraith2  = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# if wraith1.clocking == True:   오류가 발생함. 레이스1은 클로킹을 가지고 있지 않음.
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith1.name))

#메소드
# class AttackUnit :
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
        
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <=0 :
#             print("{0} : 파괴었습니다.".format(self.name))

# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# firebat1.damaged(wraith2.damage)
# firebat1.damaged(45)

#상속
# 일반유닛
class Unit :
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

# 공격유닛
class AttackUnit(Unit) :
    def __init__(self, name, hp,speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
        
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
        .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <=0 :
             print("{0} : 파괴었습니다.".format(self.name))


# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# firebat1.damaged(45)
# firebat1.damaged(45)

class Flyable:

    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))


class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed) :
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed는 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):       #메소드 오버라이딩 move 재정의(새로운 move)
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

valkyrie  = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")

#메소드 오버라이딩

vulture = AttackUnit("벌처", 80, 10, 20)
battelcruiser = FlyableAttackUnit("배틀크루져", 500, 25 ,3 )

vulture.move("11시")
#battelcruiser.fly(battelcruiser.name, "9시")
battelcruiser.move("9시")

#pass 일단은 넘어간다.(완성된 것 처럼 보인다.)

# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass
    
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()

#super 다중상속일 때 맨 처음에 상속받는 클래스(앞에 있는 매개변수)에 대해서만 상속이 됨

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init_(self, name, hp, 0)
        super().__init__(name, hp, 0) #셀프는 생략한다.
        self.location = location

# class Unit:
#     def __init__(self):
#         print("Unit 생성자")

# class Flyable:
#     def __init__(self):
#         print("Flyable 생성자")

# class FlyableUnit(Flyable, Unit):
#     def __init__(self):
#         super().__init__() #Flyable 만 상속받게 됨.

#예외처리
try:
    print("나누기 전용 계산기 입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    #nums.append(int(nums[0] /nums[1] )) 깜빡하면 IndexError 뜸
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)

#에러 발생시키기
# try:
#     print("한 자리 숫자 나누기 전용 계산기 입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("첫 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/ num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")

#사용자 정의 에러처리
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기 입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("첫 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/ num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)
#finally 마지막에 무조건 실행하게 함
finally:
    print("계산기를 이용해 주셔서 감사합니다.")


#모듈
#씨어터 모듈, 프랙티스 3 참고