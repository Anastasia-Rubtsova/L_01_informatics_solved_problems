# задача 16

weeks = 6
days_in_week = 7

flat_calendar = [0] * (weeks * days_in_week)

start_index = 6
total_days = 31

for day in range (1, total_days + 1):
    flat_calendar[start_index] = day
    start_index += 1

calendar_matrix = []
for i in range(0, len(flat_calendar), days_in_week):
    week = flat_calendar[i : i + days_in_week]
    calendar_matrix.append(week)

print(" Пн  Вт  Ср  Чт  Пт  Сб  Вс")
for week in calendar_matrix:
    
    for day in week:
        if day == 0:
            print("   ", end=" ")
        else:
            if day < 10:
                print(f" {day}", end="  ")
            else:
                print(day, end="  ")
                
    print()