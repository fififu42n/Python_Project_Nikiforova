#Найти и вывести на экран S = 1! + 2! + 3! + 4! + ... + n! (n>1)

sum = 0
fac = 1
while True:
    try:
        n = int(input("Введите целое число n (n > 1): "))
        if n > 1:
            break
        print("Число n должно быть больше 1!")
    except ValueError:
        print("Введите целое число!")

for i in range(1, n + 1):
    fac *= i  # Находим факториал числа i
    sum += fac

print(f"Сумма факториалов S = {sum}")
