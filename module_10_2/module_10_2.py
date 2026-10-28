# -- coding: utf8 --
import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        vrag = 100
        den = 0
        while vrag:
            time.sleep(1)
            vrag -= self.power
            den += 1
            print(f'{self.name} сражается {den} день (дня)..., осталось {vrag} воинов.')

        print(f'{self.name} одержал победу спустя {den} дней(дня)!"')

# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
# Вывод строки об окончании сражения