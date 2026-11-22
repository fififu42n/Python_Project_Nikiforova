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


def Arifmet(NList, K, L):
    con = 0
    sum = 0
    for i in Nlist[:K]:
        sum += i
        con += 1
    for i in Nlist[:L]:
        sum += i
        con += 1
    final_sum = sum/con
    return final_sum


n = int(input("Задайте колисчество элементов списка: "))
K = int(input("С какого элемента списка удалить значения: "))
L = int(input("До какого элемента списка удалить значения: "))

Nlist = NCreate(n)
print(f"Список с кол-во элементов N: {Nlist}")
print(f"Список с удаленными элементами под номерами {K} и {L}: {Arifmet(Nlist, K, L)}")
