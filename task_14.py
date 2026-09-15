# задача 14 

# решение через цыкл
def sum_range_for():
    start = int(input("Введите начало диапазона: "))
    end = int(input("Введите конец диапазона: "))
    total = 0
    for i in range(start, end + 1):
        total += i

    print("Рассчеты сложения чисел с диапазона: ", total)

# решение с помощью формулы Гаусса 
def sum_range():
    start = int(input("Введите начало диапазона: "))
    end = int(input("Введите конец диапазона: "))
    total = (start + end) * (end - start + 1) // 2

    print("Рассчеты сложения чисел с диапазона: ", total)

def circle_diameter():
    radius = int(input("Введите радиус окружности: "))
    diameter = radius * 2

    print("Диаметр окружности: ", diameter)

