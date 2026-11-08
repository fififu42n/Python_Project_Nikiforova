#Вариант 22 Задание 2
#Даны списки A и B одинакового размера N. Поменять местами их содержимое и вывести
#вначале элементы преобразованного списка A, а заметем - элементы преобразованного списка B
import random

def list_createA(n):
    A = []
    i = 0
    while i < n:
        A.append(random.randint(1, 100))
        i += 1
    return A

def list_createB(n):
    B = []
    i = 0
    while i < n:
        B.append(random.randint(1, 100))
        i += 1
    return B

def switch_list(A, B):
    n = A
    A = B
    B = n
    return A, B

n = int(input("Введите кол-во элементов для списков A и B: "))
A = list_createA(n)
B = list_createB(n)
print(f"Список A: {A}")
print(f"Список B: {B}")
print(f"Поменяли элементы списков местами: {switch_list(A, B)}")



