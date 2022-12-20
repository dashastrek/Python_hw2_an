#3.Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
#Пример:
#[1.1, 1.2, 3.1, 5, 10.01] => 0.19
a = [15.6, 1, 11.09, 5.12, 10.01]
for i in range(len(a)):
    import math
    x = round(a[0]-math.floor(a[0]),3)
    y = round(a[1]-math.floor(a[1]),3)
    z = round(a[2]-math.floor(a[2]),3)
    v = round(a[3]-math.floor(a[3]),3)
    n = round(a[4]-math.floor(a[4]),3)
b = [x, y, z, v, n]
print(b)
if x == 0 or y == 0 or z == 0 or v == 0 or n == 0:
    b.remove(min(b))
    print(b)
    print(max(b) - min(b))