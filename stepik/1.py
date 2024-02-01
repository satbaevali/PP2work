n = int(input())

# Создаем список нечетных натуральных чисел в интервале [n, 2n^2]
odd_numbers = [2 * i + 1 for i in range(n,n*2+1)]

# Преобразуем список в кортеж
my_tuple = tuple(odd_numbers)

# Выводим кортеж на экран
print(my_tuple)
