""""
1. Сгенерируйте с использованием функции range (случайный шаг от 3 до 5) массив,
содержащий отсортированные числа от 10 до 250 млн.
Можно использовать функцию randomint из модуля random для ещё большей
рандомизации значений, но для целей работы алгоритма бинарного поиска проследите,
чтобы значения в массиве были отсортированы.
"""

import random, time

step = random.randint(3, 5)
numbers = list(range(10, 250000001, step))
random.shuffle(numbers)
numbers.sort()

""""
2. Сгенерируйте с помощью list comprehensions и функции randomint 
(встроенный модуль random) 10 случайных чисел.
"""

random_numbers = [random.randint(1, 100) for _ in range(10)]

print(random_numbers)


# 3. Напишите функцию для алгоритма линейного поиска.

def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1


# 4. Напишите функцию для алгоритма бинарного поиска.

def binary_search(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


""""
 5. Проверьте наличие ранее сгенерированных случайных чисел в массиве 
 с помощью алгоритмов линейного и бинарного поиска, замерьте время
"""

def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

target = 500000  # Здесь можно указать любое из сгенерированных случайных чисел
result_linear, time_linear = measure_time(linear_search, numbers, target)
if result_linear != -1:
    print(f"Число {target} найдено на позиции {result_linear} с помощью линейного поиска.")
else:
    print(f"Число {target} не найдено с помощью линейного поиска.")

# Поиск с помощью бинарного поиска (предварительно отсортировав массив)
random_numbers.sort()
result_binary, time_binary = measure_time(binary_search, numbers, target)
if result_binary != -1:
    print(f"Число {target} найдено на позиции {result_binary} с помощью бинарного поиска.")
else:
    print(f"Число {target} не найдено с помощью бинарного поиска.")

# Вывод времени выполнения для обоих методов
def format_time(seconds):
    minutes = int(seconds // 60)
    seconds %= 60
    return f"{minutes} минут {seconds:.2f} секунд"

print(f"Время выполнения линейного поиска: {format_time(time_linear)}.")
print(f"Время выполнения бинарного поиска: {format_time(time_binary)}.")