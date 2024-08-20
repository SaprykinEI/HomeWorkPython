#-----Задача1---------#
#-----Условие: Напишите функцию подсчета периметра прямоугольника с двумя аргументами width и height.
# Функция должна возвращать значение.
#-----Решение

def counts_per_rectangle(width, height):
    perimetr = (width + height) * 2
    return perimetr


wdt = float(input("Введите ширину прямоугольника: "))
hgt = float(input("Введите высоту прямоугольника: "))
res = counts_per_rectangle(wdt, hgt)
print(f"Периметр прямоугольника равен: {res}")

#-----Задача2---------#
#-----Условие: Напишите функцию возведения числа в степень с двумя аргументами number и degree.
# Функция должна возвращать значение.
#-----Решение

def expon(number, degree):
    exponentiation = number ** degree
    return exponentiation


number = int(input("Введите число: "))
degree = int(input("В какую степень возводим число: "))
print(expon(number, degree))

#-----Задача3---------#
#-----Условие: Напишите функцию, подсчитывающую количество слов в введенном тексте с одним аргументом text.
# Функция должна вернуть количество слов.
#-----Решение

def get_word_counter(text):
    count = len(txt.split())
    return count


txt = input("Введите ваш текст: ")
print(get_word_counter(txt))

#-----Задача4---------#
#-----Условие: *Напишите функцию, которая принимает бесконечное количество чисел и возвращает среднеарифметическое,
# переданных чисел. Функция должна вернуть среднеарифметическое, переданных чисел.
#-----Решение

def calc_average(*args):
    aver = sum(args) / len(args)
    return aver


print(calc_average(1,2,3,4,5))


# Вариант 2

def calc_averag(*args):
    average = sum(args) / len(args)
    return average


averr = calc_averag(*map(int, input("Введите числа через пробел: ").split()))
print(averr)


sd

