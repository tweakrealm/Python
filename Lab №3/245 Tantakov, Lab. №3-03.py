print("Задание №3 \"Преобразование типов\" \n")

try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))

    summa = num1 + num2
    print("Сумма двух чисел =", summa, "\n")

except ValueError:
    print("Ошибка! Введите целое число! \n")

input("Нажмите Enter, чтобы закрыть программу...")



