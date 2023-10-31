# Створіть класи "ТранспортнийЗасіб" та два підкласи, "Автомобіль" і "Велосипед", +
# які успадковують властивості та методи батьківського класу. +
# Кожен транспортний засіб повинен мати атрибути "швидкість" та "потужність", + а також метод "прискорити", ===
# який збільшує швидкість на певну величину. Автомобіль повинен мати додатковий атрибут "пальне",
# а велосипед - "кількість педалей". Створіть об'єкти для кожного підкласу,
# змініть їх атрибути та викличте метод "прискорити" для кожного.

class Transport:
    # введіть свій код тут
    def __init__(self, speed, power):
        self.speed = speed
        self.power = power

    def accelerate(self, add_speed=0):
        self.speed = max(self.speed + add_speed, 0)


class Car(Transport):
    def __init__(self, speed, power, fuel):
        super().__init__(speed, power)
        self.fuel = fuel


speed_Car = int(input("Введіть швидкість автомобіля: "))
power_Car = int(input("Введіть потужність автомобіля: "))
fuel_Car = input("Введіть тип палива для автомобіля: ")

car = Car(speed_Car, power_Car, fuel_Car)
car.accelerate(240)
print(f'Швидкість автомобіля: {car.speed}, Потужність: {power_Car}, Пальне: {fuel_Car}')


class Bicycle(Transport):
    def __init__(self, speed, power, pedals):
        super().__init__(speed, power)
        self.pedals = pedals


speed_Bike = int(input("Введіть швидкість велосипеда: "))
power_Bike = int(input("Введіть потужність велосипеда: "))
pedals_Bike = int(input("Введіть к-ть педалей у велосипеда: "))

bike = Bicycle(speed_Bike, power_Bike, pedals_Bike)
bike.accelerate(20)
print(f'Швидкість велосипеда: {bike.speed}, Потужність: {power_Bike}, К-ть педалей: {pedals_Bike}')
