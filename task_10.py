# задача 10


def index_of_min ():
    nums = input("Введите числа через пробел: ")
    nums_array = list(map(int, nums.split()))
    print(nums_array)

    if not nums_array :
        print("Список пуст! ")
        return -1
        
    else :
        min_num = nums_array[0]
        min_index = 0

        for i, num in enumerate(nums_array):
            if num < min_num:
                min_num = num
                min_index = i

    print("Минимальное число ", min_num, " с индексом ", min_index)
    return min_index
index_of_min ()
