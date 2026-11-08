#Вариант 22 Задание 1
#Дан список размера N и целые числа K и L (1 < K <= L <= N). Найти среднее арифметическое
#всех элементов списка, кроме элементов с номерами от K до L включительно
import random

def NCreate(n):
    Nlist = []
    i = 0
    while i < n:
        Nlist.append(random.randint(1, 100))
        i += 1
    return Nlist

def Rer(K, L, Nlist):
    remove_list = [K, L]
    for i in remove_list:
        Nlist.pop(i)
    return Nlist

n = int(input("Введите число N (оно должно быть больше 2): "))
K = int(input("Введите число K (1 < K <= L): "))
L= int(input("Введите число L (K < L <= N): "))

Nlist = NCreate(n)
print(f"Список с кол-во элементов N: {Nlist}")
print(f"Список с удаленными элементами под номерами {K} и {L}: {Rer(K, L, Nlist)}")
