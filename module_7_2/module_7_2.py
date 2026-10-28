strings_positions = {}
def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding= 'utf-8')
    for i in range(0, len(strings)):
        kursor = i+1
        kursor1 = file.tell()
        file.write(strings[i])
        file.write('\n')
        strings_positions[(kursor, kursor1)] = strings[i]
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)