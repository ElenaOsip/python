# 11 Напишите программу, которая принимает на вход число N и выдает последовательность из N членов
# пример: N = 5
# 1, -3, 9, -27, 81

# import random
# n=int(input('введите число '))
# for i in range(n):
#     print(random.randrange(-100,100), end=', ')  
# or
# n=int(input('введите число '))
# a=1
# for i in range (n):
#     print(a, end=" ")
#     a=a*(-3)

# 12 Для натурального N создать словарь индекс-значение, состоящий из элементов последовательности 3N+1
# пример n = 6
# {1: 4, 2- 7, 3- 10, 4: 13, 5: 15, 6:19} 
# {0: 1, ......5:15}

# n=int(input('введите натуральное число, не более 10 '))
# for i in range (n):
#     value=int(i*3+1)
#     print(i, end=': ')
#     print(value, end=', ')
# or 
# d={a: (3*a+1) for a in range (n)}
# print(d)

# 13 Напишите программу, в которой пользователь будет вводить две строки, а программа определять количество вхождений одной строки 
# в другую

line=str(input('введите две строки '))
line2=str(input())
l=len(line)
l2=len(line2)
j=0
count=0
if l>l2:
    for i in range(l+1):
        while j<l2:
            if line2[j] == line[i]:
                j+=1
count+=1
print(count)
# else:
#     for i in range(l):
#         if line == line2:
#             count+=1
#     print(count)
# 
