
def personal_sum(numbers):
    incorrect_data = 0
    summa = 0
    result = ()
    for i in numbers:
        try:
            summa += i

        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
            incorrect_data += 1
    result = (summa, incorrect_data)
    return result

def calculate_average(numbers):

    try:
        result = personal_sum(numbers)
        summa = result[0]
        incorrect = result[1]
        result1 = summa / (len(numbers) - incorrect)
    except ZeroDivisionError:
        result1 = 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        result1 = None

    return result1


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать