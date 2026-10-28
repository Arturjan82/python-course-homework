# -- coding: utf8 --
from time import sleep
from datetime import datetime
import time
import threading

def write_words(word_count, file_name):
    for i in range(1, word_count +1):
        file = open(file_name, 'a', encoding='utf-8')
        file.write(f'Какое-то слово {i}')
        file.write('\n')
        time.sleep(0.1)
    file.close()
    return print(f'Завершилась запись в файл {file_name}')

time_start = datetime.now()
# start = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
# Взятие текущего времени
time_stop = datetime.now()
time_res = time_stop - time_start

# Вывод разницы начала и конца работы функций
print(f'Время работы функций {time_res}')

#  создаю 4 потока для вызова этой функции
# Взятие текущего времени
time2_start = datetime.now()

thread5 = threading.Thread(target = write_words, args = (10, 'example5.txt'))
thread6 = threading.Thread(target=write_words, args= (30, 'example6.txt'))
thread7 = threading.Thread(target=write_words, args= (200, 'example7.txt'))
thread8 = threading.Thread(target=write_words, args= (100, 'example8.txt'))
thread5.start()
thread6.start()
thread7.start()
thread8.start()
thread5.join()
thread6.join()
thread7.join()
thread8.join()

# Взятие текущего времени

time2_stop = datetime.now()
time2_res = time2_stop - time2_start
print(f'Время работы потоков {time2_res}')
