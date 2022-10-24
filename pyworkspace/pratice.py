# locker = {1:"park", 2:"Jung", 3:"Lee"}
# print(locker)

# print(locker.get(1))
# print(locker[2])

# print(4 in locker)
# print(2 in locker)

# locker = {"A1":"Park", "A2":"KIM"}
# print(locker)

# locker["A2"] = "Lee"
# print(locker["A2"])

# locker["A3"] = "Min"
# print(locker)

# del locker["A3"]
# print(locker)


# print(locker.keys())
# print(locker.values())
# print(locker.items())

# from random import *
user = range(1,21)
print(type(user))

user = list(user)
print(type(user))

# print(user)
# shuffle(user)
# print(user)

# winners = sample(user, 4)
# # print(winners)

# print("winner : {0}".format(winners[0:]))
# print("winner : {0}, {1}".format(winners[0], winners[1]))
# print("winner : {0}".format(winners[2:]))

# weather = input("오늘 날씨는 어때요?")
# if weather =="비" or "눈" : print("비가 옵니다.")
# elif weather =="눈" : print("눈이 옵니다.")
# else: print("날씨가 맑습니다.")

# temp = int(input("기온은 어때요?"))
# if temp >=30: print("날씨가 더워요")
# elif temp >=10 and temp <=30 : print("날씨가 너무 좋아요.")
# elif 0<temp<=10 : ("너무 추워요")
# else : print("얼어 죽어요")

# for waiting_no in range(5):
#     print("대기번호 :  {0}".format(waiting_no))

# customer = "토르"
# person = "Unknown"

# while person != customer:
#     print("{0}님 들어오세요".format(customer))
#     person = input("이름을 입력하세요 :")

# absent = [2, 5]
# no_book = [4,9]
# for student in range(1, 11, 2):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("{0} is no book".format(student))
#         break
#     print("{0}".format(student))

# student = [1,2,3,5,6]
# print(student)
# student = [i+100 for i in student]
# print(student)

# students = ["Iron man", "Thor", "Groot"]
# students = [len(i) for i in students]
# print(students)

# numbers = [i for i in range(1,50,5)]
# print(numbers)

# from random import *
# cnt =0
# for i in range(1,51):
#     time = randrange(5,51)
#     if 5 <= time <= 15:
#         print("[O] {0} 번째 손님 (소요시간 : {1}분)".format(i,time))
#         cnt+=1
#     else:
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i,time))
# print("총 탑승 승객 : {0} 분".format(cnt))

# def deposit(balance, money):
#     balance += money
#     print("{0}입금, 잔고는 {1}입니다".format(money, balance))
#     return balance

# def withdraw(balance, money):
#     if balance >= money:
#         print("{0}출금되었습니다. 잔고는 {1}입니다.".format(money, balance-money))
#         return balance-money
#     else:
#         print("출금 불가, 잔액이 모자랍니다.")
#         return balance
# balance = 1000
# balance = deposit(1000, 2000)
# balance = withdraw(balance, 5000)

# def profile(name, age, main_lang):
#     print("이름:{0}\t age:{1}\t main_lang:{2}".format(name, age, main_lang))

# profile("Park", 27, "Python")
# profile("Kim", 27, "Python")

# def profile(name, age=27, main_lang="Python"):
#     print("{0} : {1} : {2}".format(name, age, main_lang),end="")
#     print("{0} : {1} : {2}".format(name, age, main_lang))

# profile("park")
# profile("Jung")
# profile(main_lang="Java", age=28, name="Lee")

# def profile(name, age, *language):
#     print("이름 : {0}, 나이 :{1} ".format(name, age), end="")
#     for lan in language:
#         print(lan,end="")
#     print()

# profile("Park", 25, "Python  ", "Java  ", "JavaScript  ","C  ","C++  ")
# profile("Park", 25, "Python  ","C  ","C++  ")

# gun=10
# def checkpoint(soldiers):
#     global gun
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))

# print("Python", "Java", "JavaScript", sep=" vs",end="!!!")
# print("what")

# scores = {"math":0, "Eng":50, "Coding":100}
# for subject, score in scores.items():
#     print(subject.ljust(6), str(score).rjust(4), sep=":")

# for subject, score in scores.items():
#     print(subject.ljust(6), str(score).rjust(4), sep=":",end="|")

# for num in range(1,21):
#     print("{0}".format(str(num).zfill(3)) )

# answer = input("입려하신 값은?")  #입력값은 항상 문자열
# print(type(answer))
# print("입력하신 값은:{0}".format(answer))

# print("{0: >10}".format(500))
# print("{0: >+10}".format(500))
# print("{0:_>+10}".format(500))
# print("{0:*<+10}".format(-500))

# print("{0:^<+30,}".format(500000000))
# print("{0:f}".format(5/3))
# print("{0:.2f}".format(5/3))

# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 90", file=score_file)
# print("영어 : 100", file=score_file)
# score_file.close()

# score_file = open("score.txt","a", encoding="utf8")
# score_file.write("과학 : 70")
# score_file.write("\n국어 :100")
# score_file.close()

# score_file = open("score.txt","r", encoding="utf8")
# print(score_file.read())

# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")

# score_file = open("score.txt","r",encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line,end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines()
# for line in lines:
#     print(line, end="")

# score_file.close() 

# import pickle
# # profile_file = open("profile.pickle", "wb")
# # profile = {"이름":"박명수", "나이":30, "취미":["축구","농구","코딩","배드민턴"]}
# # print(profile)
# # pickle.dump(profile, profile_file)
# # profile_file.close()

# profile_file = open("profile.pickle","rb")
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

# import pickle
# with open("profile.pickle","rb") as profile_file:
#     print(pickle.load(profile_file))

# import pickle
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요!")

# with open("study.txt","r",encoding="utf8") as study_file:
#     print(study_file.read())

# import pickle

# for n in range(1,51):
#     # with open("{0}주차.txt".format(n), "w", encoding="utf8") as file:
#     with open(str(n) + "주차.txt", "w", encoding="utf8") as file:
#         file.write("- {0}주차 주간 보고 -".format(n))
#         file.write("\n 부서:")
#         file.write("\n 이름:")
#         file.write("\n 업무:")



# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# # marine1 = Unit("마린", 40, 5)
# # marint2 = Unit("마린", 40, 5)
# # tank = Unit("탱크", 150, 35)

# #레이스 : 공중 유닛
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 {1}".format(wraith1.name, wraith1.damage))

# wraith2 = Unit("레이스2",80, 5)
# wraith2.clocking = True

# #객체에 멤버 변수 추가(wraith2에만 생성) 
# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))


# #일반 유닛
# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# #공격 유닛
# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp 
#         self.damage = damage
    
#     def attack(self, location):
#         print("{0} : {1}방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
#         if self.hp <= 0 :
#             print("{0} : 파괴 되었습니다.".format(self.name))

# firebat1 = AttackUnit("파이어벳", 50, 16)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)


# #일반 유닛
# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp

# #공격 유닛 (상속)
# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage
    
#     def attack(self, location):
#         print("{0} : {1}방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
#         if self.hp <= 0 :
#             print("{0} : 파괴 되었습니다.".format(self.name))

# firebat1 = AttackUnit("파이어벳", 50, 16)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)

# #일반 유닛
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed

#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

# #공격 유닛 (상속)
# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage, speed):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1}방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
#         if self.hp <= 0 :
#             print("{0} : 파괴 되었습니다.".format(self.name))

# #날 수 있는 유닛 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("[공중 유닛 이동]")
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# #공중 공격 유닛
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, damage, 0 )
#         Flyable.__init__(self, flying_speed)

# # move() 메소드 재정의
#     def move(self, location):
#         self.fly(self.name, location)

# #벌쳐 : 지상 유닛
# vulture = AttackUnit("벌쳐", 80, 10 , 20)

# #배틀크루저 : 공중 유닛
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# battlecruiser.move("9시")


# #일반 유닛
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed

#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

# #공격 유닛 (상속)
# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage, speed):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1}방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
#         if self.hp <= 0 :
#             print("{0} : 파괴 되었습니다.".format(self.name))

# #날 수 있는 유닛 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("[공중 유닛 이동]")
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# #공중 공격 유닛
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, damage, 0 )
#         Flyable.__init__(self, flying_speed)

# # move() 메소드 재정의
#     def move(self, location):
#         self.fly(self.name, location)

# # pass : 일단은 아무처리 없이 넘어 감
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#     #    pass
#     # Unit.__init__(self, name, hp, 0)
#     super().__init__(name, hp, 0) #super 사용시 self는 쓰지 않음.

# # 서플라이 디폿 : 건물, 건물 1개 = 8 유닛
# #supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# # def game_start():
# #     print("[알림]새로운 게임 시작!")

# # def game_over():
# #     pass #아무 처리 없이 지나감

# # game_start()
# # game_over()

# 스타크래프트 기능 추가 및 보완

# from random import *

# #일반 유닛
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다".format(name))

#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))
    
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
#         if self.hp <= 0 :
#             print("{0} : 파괴 되었습니다.".format(self.name))

# #공격 유닛 (상속)
# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage, speed):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1}방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))

# # 마린
# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40, 1, 5)

#     #스팀팩 : 일정 지간 동안 이동 및 공격 속도를 증가, 체격은 10감소
#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -= 10
#             print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
#         else:
#             print("{0} : 체력이 부족하여 스팀팩을 사요할 수 없습니다.".format(self.name))

# class Tank(AttackUnit):
#     #시즈모드 : 탱크 고정, 높은 공격력, 이동 불가
#     seize_developed = False #시즈모드 개발 여부
    
#     def __init__(self): 
#         AttackUnit.__init__(self, "탱크", 150, 1, 35)
#         self.seize_mode = False
    
#     def set_seize_mode(self):
#         if Tank.seize_developed == False:
#             return
        
#         # 현재 지스모드가 아닐 때 -> 시즈모드 변경
#         if self.seize_mode == False:
#             print("{0} : 시즈모드로 전환합니다.".format(self.name))
#             self.damage *= 2
#             self.set_seize_mode = True
#         else:
#             print("{0} : 시즈모드를 해제합니다.".format(self.name))
#             self.damaged /= 2
#             self.set_seize_mode = False

# #날 수 있는 유닛 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("[공중 유닛 이동]")
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# #공중 공격 유닛
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, damage, 0 )
#         Flyable.__init__(self, flying_speed)

# # move() 메소드 재정의
#     def move(self, location):
#         self.fly(self.name, location)

# # 레이스
# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
#         self.clocked = False #클로킹 모드 (해제 상태)

#     def clocking(self):
#         if self.clocked == True:
#             print("{0} : 클로킹 모드 해제합니다.".format(self.name))
#             self.clocked = False
#         else:
#             self.clocked = True
#             print("{0} : 클로킹 모드 설정합니다.".format(self.name))

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     print("Player : gg")
#     print("[Player] 님이 게임에서 퇴장하셨습니다.")

# # 게임 시작
# game_start()

# # 유닛 생성
# m1 = Marine()
# m2 = Marine()
# m3 = Marine()

# t1 = Tank()
# t2 = Tank()

# w1 = Wraith()

# # 리스트에 유닛 추가 (유닛 일괄 관리)
# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t2)
# attack_units.append(w1)

# # 전군 이동
# for unit in attack_units:
#     unit.move("1시")

# # 탱크 시즈모드 개발
# Tank.seize_developed = True
# print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# # 공격 모드 준비 (마린: 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
# for unit in attack_units:
#     if isinstance(unit, Marine):
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.set_seize_mode()
#     elif isinstance(unit, Wraith):
#         unit.clocking()

# # 전군 공격
# for unit in attack_units:
#     unit.attack("1시")

# # 전군 피해
# for unit in attack_units:
#     unit.damaged(randint(5, 21)) # 공격을 랜덤으로 받음(5 ~ 20)

# # 게임 종료
# game_over()

# 예외처리

# try:
#     print("나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     print("{0} 나누기 {1} : {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("에러! 잘못된 값을 입력했습니다.")
# except ZeroDivisionError as err:
#     print(err)

# try:
#     print("나누기 전용 계산기입니다.")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
#  #   nums.append(int(nums[0] / nums[1]))
#     print("{0} 나누기 {1} : {2}".format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("에러! 잘못된 값을 입력했습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except IndexError as err:
#     print(err)
# except:
#     print("알 수 없는 에러!")
# except Exception as err:
#     print("알 수 없는 에러!")
#     print(err)

# 에러 발생시키기
# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")

# 사용자 정의 에러

# class BingNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise BingNumberError("입력값 : {0}, {1}".format(num1, num2))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except BingNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
#     print(err)
# finally:
#     print("계산기를 이용해 주셔서 감사합니다.")

# class SoldOutError(Exception):
#     pass

# chicken = 10
# waiting = 1
# while(True):
#     try:
#         print("[남은 치킨 :{0}]".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#         if order > chicken:
#             print("재로가 부족합니다.")
#         elif order <=0 :
#             raise ValueError
#         else:
#             print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting, order))
#             waiting +=1
#             chicken -=order
#         if chicken ==0:
#             raise SoldOutError
#     except ValueError:
#         print("잘못된 값을 넣었습니다.")
#     except SoldOutError:
#         print("재고가 소진되었습니다.")
#         break


# 모듈

# import theater_module
# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(5)

# import theater_module as mv   # 모듈 이름에 별칭 사용
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *  # 모듈을 import해서 바로 함수 이름만으로 사용
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning #사용할 함수만 import 할 수 있음
# price(3)
# price_morning(4)

# from theater_module import price_soldier as ps
# ps(5)

# import travel.thailand
# trip_to = travel.thailand.thailandPackage()
# trip_to.detail()