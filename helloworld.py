print("hello world")
python = ['python', 'is', 'easy']
print(python[1:])
print(python[:3])
print(python[-4:])
print(python[1::1])
print(python[1::-1])

python = "Python is Amazing"
print(python[0].isupper())
print(len(python))
index = python.index("n") # index라는 변수에 python 변수안에 들어있는 n의 인덱스 값을 넣어줬다.
print(index)
print("a" + "b") #ab
print("a", "b")
print("나는 {}색과 {}색을 좋아해요" .format("파란", "빨간")) # 2개된다
print("Red Apple\rPine") # pine Apple
print("Redd\bApple")

students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)

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

open_account()
balance = 0 # 잔액
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000)
print(balance)
balance = withdraw(balance, 500)
print(balance)
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이며 잔액은{1}원 입니다".format(commission, balance))

def profile3(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end =" ")
    print()

profile3("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile3("김태호", 25, "Kotlin", "Swift")

print("{0:^<+15,}".format(100000000))
print("{0:f}".format(5/3))
print("{0:.2f}".format(5/3))

class BuildingUnit():
    def __init__(self, name, hp, location):
        pass
    
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")
print(supply_depot)

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()