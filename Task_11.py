# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# Пример, для N = 5: 1, -3, 9, -27, 81.

N = int(input('Введите значение N = '))
list = []
out = 1
for i in range(1, N + 1,):
    list.append(out)
    out *= -3
print(f'Для N = {N}: {list}')