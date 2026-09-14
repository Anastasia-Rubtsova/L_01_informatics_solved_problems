# задача 2

def bytes_to_kilobytes ():
    bytes_value = float(input("Введите байты, для того чтобы их перевести в килобайты: "))
    k_bytes_value = bytes_value / 1024
    print("Байты переведенные в килобайты: ", k_bytes_value)

def kilobytes_to_bytes ():
    k_bytes_value = float(input("Введите килобайты, для того чтобы их перевести в байты: "))
    bytes_value = k_bytes_value * 1024
    print("Килобайты переведенные в байты: ", bytes_value)

bytes_to_kilobytes ()
kilobytes_to_bytes ()
