# Задача 1/6
# Напишите программу, которая принимает на вход цифру, обозначающую день недели и проверяет является ли этот день выходным
print('Задача 6')
print('введите любую цифру от 1 до 7, обозначающую день недели')
a=int(input())
if a==6 or a==7:
    print('выходной')
else: print('рабочий')

# Задача 2/7
# Напишите программу для проверки истинности утверждения 
#  ⌝ (X v Y v Z) = ⌝ X ⌃ ⌝ Y ⌃ ⌝ Z для всех значений предикат
print()
print('Задача 7')
print()
print('Вариант 1')
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2): 
            if not(x or y or z)==(not x and not y and not z):
                print ('true')
            else: print ('false')
# or 
# 
print()
print('Вариант 2')
print()
count=0
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2): 
            if not(x or y or z)==(not x and not y and not z):
                count=count+1
if count==2**3:
    print('true')
else: print('false')
     

# Задача 3/8
# Напишите программу, которая принимает на вход координаты точки (X и Y), причем X и Y не равно 0 и выдает 
# номер четверти плоскости, в которой находится эта точка 
print()
print('Задача 8')
print()
print('введите координаты точки')
x=int(input())
y=int(input())
if x>0 and y>0:
    print('точка находится в первой четверти плоскости')
elif x>0 and y<0:
    print('точка находится в четвертой четверти плоскости')
elif x<0 and y>0:
    print('точка находится во второй четверти плоскости')
else: print('точка находится в третьей четверти плоскости')


# Задача 4/9
# Напишите программу, которая по заданному номеру четверти показывает диапазон возможных координат точек в этой четверти (x и y)
print()
print('Задача 9')
print()
print('введите номер четверти, в которой находится точка')
a=int(input())
if a==1:
    print('координаты точки находятся где то в пространстве где x & y >0')
elif a==2:
    print('координаты точки находятся где то в пространстве где x<0 & y>0')
elif a==3:
    print('координаты точки находятся где то в пространстве где x&y<0')
else: print('координаты точки находятся где то в пространстве где x>0 & y<0')

# 
# 
# Задача 5/10
# Напишите программу, которая принимает на вход координаты двух точек и и находит расстояние между ними в 2D пространстве 
# example:
# A (3,6) B(2,1) -- 5.09
# A (7,-5) B(1,-1) -- 7.21
print()
print('Задача 10')
print()
print('введите координаты первой точки')
x=int(input())
y=int(input())
print('введите координаты второй точки')
x1=int(input())
y1=int(input())

sqrt = (x1-x)**2 + (y1-y)**2
dist = str (sqrt**(1./2))
print("расстояние между точками = ", end = ' ' + dist)
