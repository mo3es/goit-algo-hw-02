from collections import deque

d = deque()

#Запит строки, що перевіряється на паліндром
processed_string = input("Введіть строку для перевірки\n")

#Приведення строки до єдиного регістру та очистка від пробілів
final_string = processed_string.lower().replace(" ", "").replace("\t", "").replace("\n", "")

#Посимвольно вводимо аналізовану строку у чергу
for char in final_string:
    d.append(char)

#Порівнюємо символи в кінці та на початку черги, у разі неспівпадіння - строка не є паліндромом
end = len(d) // 2
for i in range(0, end):
    char_1 = d.pop()
    char_2 = d.popleft()
    if  char_1 != char_2:
        print("Строка не є паліндромом")
        quit()
print("Строка є паліндромом")
