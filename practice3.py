print("Задача 22. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях")
# Пример:
# • [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

n=int(input('введите длину списка  '))
import random
spisok = []
for i in range(n):
    spisok.append(random.randint(0,100))
sum=0
print(spisok)
for i in range(n):
    if i%2 !=0:
        sum = sum+ spisok[i]
print(sum)
print()


print("23. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.")
# Пример:
# • [2, 3, 4, 5, 6] => [12, 15, 16];
# • [2, 3, 5, 6] => [12, 15]

n=int(input('введите длину списка  '))
import random
spisok = []
for i in range(n):
    spisok.append(random.randint(0,10))
import math
print(spisok)

spisok1=[]
m=math.ceil(n/2)-1

for i in range(math.ceil(n/2)):
    spisok1.append(spisok[i]*spisok[n-i-1])

print(spisok1)
print()

print ("24. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.")
# Пример:
# • [1.1, 1.2, 3.1, 5, 10.011 => 0.19
# x=[1.1, 1.2, 3.1, 5, 10.01]
n=int(input('введите длину списка  '))
import random
x=[round(random.uniform(1, 100), 3) for x in range(n)]
print(x)
spisok=[]
import math
for i in range (n):
    if type(x[i])==float:
        spisok.append(round(x[i]-int(x[i]), 3))

difMaxMin=max(spisok)-min(spisok)
print(max(spisok)-min(spisok))
print()

print("25. Напишите программу, которая будет преобразовывать десятичное число в двоичное.")
# Пример:
# • 45 -> 101101
# • 3 -> 11
# • 2 -> 10

n=int(input('введите 10ое число, которое вы хотите перевести в двоичное '))
spisok=[]
if n!=0:
    while n>=2:
        spisok.append(n%2)
        n=int(n/2)
        spisok.append(1)
      
else: print("0 в двоичной системе = 0")

spisok.reverse()

for i in spisok:
    print(i,end = ' ')
print()
print()

print("26. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.")

n=int(input('введите число для списка чисел Фибоначчи & more '))

fib_list=[0,1]
i=2
while i<=n:
    fib_list.append(fib_list[i-1]+fib_list[i-2])
    i+=1

nega_fib = []

i=-n
if n%2==0:
    while i <=-1:
        nega_fib.append(round((-1)**(i)*fib_list[i]))
        i+=1
else: 
    while i <=-1:
        nega_fib.append(round((-1)**(i+1)*fib_list[i]))
        i+=1

nega_fib.reverse()

print(nega_fib+fib_list)
