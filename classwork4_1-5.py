#task_1
import math
def rectangle():
    x=int(input("сторона прямокутника а="))
    y=int(input("сторона прямокутника b="))
    return print(x*y)
def circle():
    r=int(input("радіус кола r="))
    return print(3.14*r**2)
def triangle():
    a=int(input("сторона трикутника a="))
    b=int(input("сторона трикутника b="))
    c=int(input("сторона трикутника c="))
    p=(a+b+c)/2
    return print(math.sqrt(p*(p-a)*(p-b)*(p-c)))

a=int(input('''Для обчислення площі прямокутника введіть 1
 площі трикутника 2
 площі кола 3 \n'''))
if a==1:
    rectangle()
elif a==2:
    triangle()
elif a==3:
    circle()
else: print("input error")

#task_2

def sum(n):
    s=0
    while n!=0:
        s+=n%10
        n=int(n/10)
    return s
a=int(input("input number "))
print(sum(a))

#task_3
def addition (a,b):
    return a+b
def subtraction (a,b):
    return a-b
def multiplication (a,b):
    return a*b
def division (a,b):
    return a/b
loop=1
while loop==1:
    a=int(input('''Виберіть дію:
1 - додавання
2 - віднімання
3 - множення 
4 - ділення
5 - вихід \n'''))
    if a==1:
        print("Функція додавання")
        b=float(input("введіть перше число \n"))
        c=float(input("+ \n введіть друге число \n"))
        print ("Сумма = ", addition(b,c))
    elif a==2:
        print("Функція віднімання")
        b=float(input("введіть перше число \n"))
        c=float(input("- \n введіть друге число \n"))
        print ("Різниця = ", subtraction(b,c))
    elif a==3:
        print("Функція множення")
        b=float(input("введіть перше число \n"))
        c=float(input("* \n введіть друге число \n"))
        print ("Добуток = ", multiplication(b,c))
    elif a==4:
        print("Функція ділення")
        b=float(input("введіть перше число \n"))
        c=float(input("/ \n введіть друге число \n"))
        print (" = ", division(b,c))
    elif a==5:
        print("Виконання програми завершено")
        break

#task_4

def fibonacci(a):
    m=0
    n=1
    s=0
    print('Числа фібоначі до числа ', a)
    while m<a:
        print (m)
        s=m+n
        n=m
        m=s
f=int(input("Введіть число  "))
fibonacci(f)

#task_5

def discriminant(a,b,c):
    print((b**2)+(4*a*c))
a=float(input('Введіть число a='))
b=float(input('Введіть число b='))
c=float(input('Введіть число c='))
discriminant(a,b,c)