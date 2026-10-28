import random
first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x,y: x == y, first, second)))

def get_advanced_writer(file_name):
    file = open(file_name, 'w')
    def write_everything(*data_set):
        for i in data_set:
            file.write(str(i)+'\n')
        file.close()
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

from random import choice
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        result = random.choice(self.words)
        return result

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())


