# задача 3
def is_divisor ():
    a = int(input("Введите число делитель: "))
    b = int(input("Введите число делимое: "))
    if b % a == 0:
        print(True)
    else:
        print(False)

is_divisor ()