import os
import time

directory = '.'
# for i in os.walk(r'C:\Users\user\PycharmProjects\pythonProject1\Python new\Homework\module7'):
#    print(i)
# print(os.path.join('home', 'User', 'Desktop', 'file.txt'))
# mod_time = os.path.getmtime('test.txt')
# mod_time_str = time.ctime(mod_time)
# print(mod_time_str)
# print(os.path.getsize('test.txt'))
# print(os.path.dirname(r'C:\Users\user\PycharmProjects\pythonProject1\Python new\Homework\module7\test.txt'))
# for root, dirs, files in os.walk(r'C:\Users\user\PycharmProjects\pythonProject1\Python new\Homework\module7'):
#     for name in files:
#         print(root + "/" + name)

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.getcwd()
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time},'
               f'Родительская директория: {parent_dir}')

        # if file.endswith('.txt'):
        #     print(os.path.join(root, file))
# for root, dirs, files in os.walk(directory):
# print(os.getcwd())
# # os.mkdir('second')
# if os.path.exists('second'):
#     os.chdir('second')
# else:
#     os.mkdir('second')
#     os.chdir('second')
# # os.makedirs(r'third\fourth')
# print(os.listdir())
# # for i in os.walk('.'):
# #     print(i)
# os.chdir(r'C:\Users\user\PycharmProjects\pythonProject1\Python new\Homework\module7\second')
# print(os.getcwd())
# print(os.listdir())
# os.chdir(r'C:\Users\user\PycharmProjects\pythonProject1\Python new\Homework\module7')
# file = [f for f in os.listdir() if os.path.isfile(f)]
# dirs = [d for d in os.listdir() if os.path.isdir(d)]
# print(file)
# print(dirs)