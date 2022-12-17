# 11 Напишите программу, которая принимает на вход число N и выдает последовательность из N членов
# пример: N = 5
# 1, -3, 9, -27, 81

# import random
# n=int(input('введите число '))
# for i in range(n):
#     print(random.randrange(-100,100), end=', ')  
# # or
# n=int(input('введите число '))
# a=1
# for i in range (n):
#     print(a, end=" ")
#     a=a*-3

# 12 Для натурального N создать словарь индекс-значение, состоящий из элементов последовательности 3N+1
# пример n = 6
# {1: 4, 2- 7, 3- 10, 4: 13, 5: 15, 6:19} 
# {0: 1, ......5:15}

# n=int(input('введите натуральное число, не более 10 '))
# for i in range (n):
#     value=int(i*3+1)
#     print(i, end=': ')
#     print(value, end=', ')
# #or 
# d={a: (3*a+1) for a in range (n)}
# print(d)
# or

# a={}
# for i in range (1,n+1):
#     a[i] = i*3+1
# print(a)

# 13 Напишите программу, в которой пользователь будет вводить две строки, а программа определять количество вхождений одной строки 
# в другую

# line1=str(input('введите две строки '))
# line2=str(input())
# count=0
# for i in range(len(line1)-1):
#     if line1[i:i+len(line2)]==line2:
#         count+=1
# print(count)

# or

# print(line1.count(line2))

# 14 Создать список случайных чисел. Найти максимальное количество одинаковых элементов. 10 в диапазоне от 2 до 5

# list=[]
# import random
# for i in range(10):
#     list.append(random.randrange(2,5))
# print(list)
# max=0
# for i in range(10):
#     if list.count(list[i])>max:
#         max=list.count(list[i])
# print(max)

# or
# import random
# list=[]
# max=0
# for i in range(10):
#     a = random.randint(2,5)
#     list.append(a)
# print(list)
# for i in set(list):
#     if list.count(i)>max:
#         max=list.count(i)
# print(max)



  
# 15 Пользователь вводит число N, программа ввыводит N строк, начиная с N * по убыванию

# n = int(input('введите любое натуральное число '))
# for i in range(n, 0, -1):
#     print('*'*i)

# or

# n = int(input('введите любое натуральное число '))
# for i in range(n):
#     print('*'*n)
#     n-=1


