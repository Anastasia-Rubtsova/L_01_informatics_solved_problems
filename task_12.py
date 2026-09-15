# задача 12

def shortest_distance(kilometers, meters):
    # Переводим километры в метры (1 км = 1000 метров)
    km_in_meters = kilometers * 1000
    
    # С помощью условной конструкции находим наименьшее
    if km_in_meters < meters:
        return km_in_meters
    else:
        return meters


user_km = float(input("Введите расстояние в километрах: "))
user_m = float(input("Введите расстояние в метрах: "))

result = shortest_distance(user_km, user_m)

print(f"Наименьшее расстояние в метрах: {result}")
