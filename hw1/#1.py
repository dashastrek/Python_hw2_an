#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и
#проверяет, является ли этот день выходным.

n = int(input('write a number '))
if n >= 1 and n < 6:
    print('no')
elif n >= 6 and n <= 7:
    print('yes')
else:
    print ('write numbers from 1 to 7')
