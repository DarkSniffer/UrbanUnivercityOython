from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name, power):
        Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies = 100

    def run(self):
        print(f"{self.name}, на нас напали!")
        days = 0
        while self.enemies > 0:
            self.enemies -= self.power
            if self.enemies < 0:
                self.enemies = 0
            days += 1
            sleep(1)
            print(f"{self.name} сражается {days} день(дня)..., осталось {self.enemies} воинов.")
        print(f"{self.name} одержал победу спустя {days} дней(дня)!")

# Создаем и запускаем 2 потока
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

# Выводим сообщение об окончании битв
print("Все битвы закончились!")