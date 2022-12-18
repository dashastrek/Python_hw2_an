#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z (расшифровка
#этого выражения not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2]) для всех значений предикат.

#for x in range(2):
 #       for y in range(2):
  #          for z in range(2):
   #            print(not (x or y or z) == (not x and not y and not z))
    #             print(x, y, z)
x = int(input('Введите число x '))
y = int(input('Введите число y '))
z = int(input('Введите число z '))
a = not(x or y or z)
b = not x and not y and not z
result = a == b
if result == True:
     print('Утверждение истинно')
else:
     print('Утверждение ложно')
     