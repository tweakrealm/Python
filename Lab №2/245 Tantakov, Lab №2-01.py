print("Задача №1 \n")

radius_cyl = float(input("Радиус основания цилиндра: "))
height_cyl = float(input("Высота цилиндра: "))
density_cyl = float(input("Плотность материала: "))
print()

import math
V_cyl = math.pi * radius_cyl**2 * height_cyl
M_cyl = V_cyl * density_cyl
S_cyl = math.pi * radius_cyl**2

print(f"Объём цилиндрического тела: {V_cyl}")
print(f"Масса цилиндрического тела: {M_cyl}")
print(f"Площадь цилиндрического тела: {S_cyl}" "\n")

input("Нажмите Enter, чтобы закрыть программу...")