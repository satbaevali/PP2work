a=int(input())
b=["Дракон", "Змея", "Лошадь", "Овца", "Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц"]
animal_index=(a-2000)%12
print(b[animal_index])