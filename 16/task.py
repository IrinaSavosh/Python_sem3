# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X

import random

n = int(input("Введите количество элементов списка: "))
x = int(input("Введите искомое число: "))
arr=[random.randint(0, 999) for i in range(n)]
print(arr)


count = 0
for i in range(len(arr)):
   while arr[i] > 9:
      temp = arr[i] % 10
      arr[i] //= 10
      if temp == x:
         count += 1
   if arr[i] == x:
      count += 1

print(count)