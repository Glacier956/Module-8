print('Задача 5. Функция 2')

# В прошлый раз мы написали Саше программу, которая считает функцию в каждой точке отрезка и с нужным шагом, начиная с конца (от большего значения X к меньшему), выводит ответ на экран. Но теперь ему нужно, чтобы значения считались в обратном порядке. Также Саше важно настроить шаг, с которым он скачет по точкам отрезка.

# Напишите программу, которая получает на вход начало и конец отрезка, а также шаг. Затем высчитывает функцию y в каждой точке отрезка и с нужным шагом, начиная с конца, выводит ответ на экран.

# Сама функция выглядит так:
# y = x**3 + 2*x**2 - 4x + 1

# Пример:
# 
# Введите начало отрезка: -2
# Введите конец отрезка: 2
# Введите шаг: -1
# В точке 2 функция равна 9
# В точке 1 функция равна 0
# В точке 0 функция равна 1
# В точке -1 функция равна 6
# В точке -2 функция равна 9

begin_segment = int(input("Введите начало отрезка: "))
end_segment = int(input("Введите конец отрезка: "))
step = int(input("Введите шаг: "))
y = 0

for x in range(end_segment, begin_segment - 1, step):
  y = (x ** 3) + 2 * (x ** 2) - (4 * x) + 1
  print("В точке", x, "функция равна", y)