class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

# 다중 상속시 앞에 있는 부모클래스의 생성자를 호출한다.
# 모든 부모클래스의 생성자를 호출할 때에는 각각의 클래스의 생성자를 모두 자식 클래스에서 호출한다.
# class FlyableUnit(Unit, Flyable):
#     def __init__(self):
#         super().__init__()

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        Unit.__init__(self)
        Flyable.__init__(self)

dropship = FlyableUnit()