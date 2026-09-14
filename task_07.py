# задача 7
def compare ():
    m = int(input("Введите число m для сравнения: "))
    n = int(input("Введите число n для сравнения: "))
    if m > n:
        print("Number m > n")
    elif m < n : 
        print("Number m < n")
    else:
        print("The numbers are equal")

compare ()