# Задача1/14

print('Задача 1/14:')
print('Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр')
# пример: 6782 -- 23; 0.56 -- 11')


n=input('введите вещественное число ')
suma=0
for i in n:
    if i.isdigit():
        suma+=int(i)
print('сумма цифр введенного числа =', end = ' ')
print(suma) 
print()


print('Задача 2/15:')
print('Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N')
# пример N = 4 -- [1,2,6,24] = [1, 1*2, 1*2*3, 1*2*3*4]
# факториал

n=int(input('введите натуральное число N '))
fact=1
print('набор произведений чисел от 1 до N =')
for i in range(1,n+1):
    fact*=i
    print(fact, end=' ')

print()
print()

print('Задача 3/16:')

print('Задайте список из чисел последовательности (1+1/n) в степени n и выведите на экран их сумму')
# пример
# для n = 4: 
# {1:2, 2:2.25, 3:2.37, 4:2.44} сумма 9.06
sum=0
n=int(input('введите вещественное число '))
for i in range (1,n+1):
    x=round((1+1/i)**i, 2)
    sum=sum+x
    print(i, end=': ')
    print(x, end=', ' )
print('\n', 'сумма чисел последовательности = ', sum)
print()


# Задача 4/17
# Задайте список из N элементов, заполненных числами из промежутка [-N,N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число

print('Задача 5/18:') 
print('Реализуйте алгоритм перемешивания списка')


n=int(input('введите длину списка '))
print()
import random
ar = []
for i in range (n):
    ar.append(random.randint(0,100))
print('original list:')
print (ar)
print()
print('shuffle list (shuffle method)')
random.shuffle(ar)
print(ar)
print()
for i in range(len(ar)-1,0,-1):
    j=random.randint(0,i+1)
    ar[i],ar[j]=ar[j],ar[i]
print('shuffle list (Fisher-Yates Algoritm)')
print(ar)

# from turtle import Turtle
# t= Turtle()
# for step in range(36):
#     t.forward(400)
#     t.right(170)
