def max_of_three ():
    a = int(input("Введите число a для сравнения: "))
    b = int(input("Введите число b для сравнения: "))
    c = int(input("Введите число c для сравнения: "))

    max_num = a

    if b > max_num:
        max_num = b
    if c > max_num:
        max_num = c
    # можно решить еще через встроенную функцию или сортировку

    print("Наибольшее число: ", max_num)
        
max_of_three ()