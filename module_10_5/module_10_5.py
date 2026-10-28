# -- coding: utf8 --
from datetime import datetime
import time
import multiprocessing
from multiprocessing import Pool

def read_info(name):
    all_data = []
    file = open(name,'r')
    while True:
        line = file.readline()
        if not line:
            break
        all_data.append(line)
    file.close()

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
# # Линейный вызов
    time_start = datetime.now()
    for file in filenames:
        read_info(file)
    time_stop = datetime.now()
    time_res = time_stop - time_start
    print(f'Линейный вызов: {time_res}')

# Многопроцессный
    time_start = datetime.now()
    with Pool(4) as p:
        p.map(read_info, filenames)
    time_stop = datetime.now()
    time_res = time_stop - time_start
    print(f'Многопроцессный вызов: {time_res}')
