# задача 8

def century_message ():
    name = input("Введите свое имя: ")
    age = int(input("Введите свой возраст: "))
    
    from datetime import date
    current_year = date.today().year

    if age >= 100:
        print(f"Тебе {name}, уже 100 лет или даже больше")
    else:
        current_year = current_year + (100 - age)
        print(f"Тебе {name}, исполнится 100 лет в {current_year}")

century_message ()
