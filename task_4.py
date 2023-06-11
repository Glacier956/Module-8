print('Задача 4. Отрезок')

# Напишите программу, которая считывает с клавиатуры три числа a, b и c, считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a; b], кратных числу c.

first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))
third_number = int(input("Введите третье число: "))

summ = 0
count = 0

for list in range (first_number, second_number + 1):
  if list % third_number == 0:
    summ += list
    count += 1
if count == 0:
  print("Расчет невозможен")
else:
  print("Cреднее арифметическое всех чисел из отрезка [" + str(first_number) + ", " + str(second_number) + "]: " + str(summ // count))
