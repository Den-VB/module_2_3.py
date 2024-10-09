# Задача "Нули ничто, отрицание недопустимо!"
my_list = [2, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
length = len(my_list)
counter = -1
while counter < length-1: # цикл с ограничением в длину списка
    counter = counter + 1
    if my_list[counter] > 0: # условие положительных чисел
        print("Положительное число", counter + 1, " = ", my_list[counter])
    elif my_list[counter] < 0: # условие отрицательных чисел
        print("СТОП! Oтрицание недопустимо!")
        break


