import random

def find_guests_order(seats):
    n = len(seats)
    result = [0] * n

    for k in range(n):
        result[seats[k] - 1] = k + 1
    return result

N = int(input("Введите количество мест, которые будут занимать гости: "))

if N < 2000:
    random_seats = random.sample(range(1, N + 1), N)

    guests_order = find_guests_order(random_seats)

    print("Рандомные места (вход):", random_seats)
    print("Кто где сидит (ответ):  ", guests_order)
else:
    print("Неверное количество мест, больше либо ровно 2000  ")
    return 0
