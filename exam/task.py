"""
Задание 1

Генератор последовательности Фибоначчи до n-го числа (включительно).
    
Аргументы:
n -- номер числа в последовательности Фибоначчи, на котором следует остановиться.
"""

def fib(n):
    
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# for num in fib(10):
#     print(num)

"""
Преобразует римское число в десятичное целое число.
    
    Аргументы:
    s -- строка, представляющая римское число.
    
    Возвращает:
    Десятичное целое число.
"""

def roman_to_int(s):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in reversed(s):
        value = roman_values[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    
    return total

# print(roman_to_int("III"))    
# print(roman_to_int("LVIII"))  
# print(roman_to_int("MCMXCIV"))

"""
    Проверяет, является ли массив монотонным.
    
    Аргументы:
    nums -- массив целых чисел.
    
    Возвращает:
    True, если массив монотонный, иначе False.
    """

def is_monotonic(nums):
    if not nums:
        return True
    
    increasing = decreasing = True
    
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            decreasing = False
        if nums[i] < nums[i - 1]:
            increasing = False
    
    return increasing or decreasing

# Примеры использования:
print(is_monotonic([1, 2, 2, 3]))   
print(is_monotonic([6, 5, 4, 4]))   # Output: True (монотонно убывающий)
print(is_monotonic([1, 3, 2]))      # Output: False (не монотонный)
print(is_monotonic([1, 1, 1, 1]))   # Output: True (монотонно возрастающий)