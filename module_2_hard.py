x = int(input('Введите число в диапазоне от 3 до 20: ')) # Выводим строку с приглашением ввести число
                                                        # и запоминаем это число в переменной x.


    # Объявляем переменные.
first_num = []  #  Список чисел для первого слагаемого нужной суммы.
second_num = [] # Список чисел для второго слагаемого нужной суммы.
un_num = []     # Список чисел, которые не входят в нужный нам перечень.
main_num = []   # Список пар чисел, которые нам необходимы.
i = 1
j = 1
for i in range(1,x): # Перебираем все числа в диапазоне x.
    num_1 = True    # Назначаем переменной значение True.
    for j in range(1,i): # Перебираем каждое значение из первого цикла.
        if i + j == x or x % (i + j) == 0:  # Проверяем сумму i и j на равенство и кратность введенному числу.
            num_1 = False # Если условие выше истинно, то присваиваем переменной num значение False и переходим
                          # к следующему шагу, если ложь, то возвращаемся к началу цикла.
            break   # Прерываем цикл и переходим к следующему шагу программы.
    if num_1:       # Проверяем переменную num_1, если True, переходим к следующиму шагу, если False,
                    # то переходим на else.
        continue
    else:
        first_num.append(i) # Добавляем значение i в список first_num.
        second_num.append(j)    # Добавляем значение j в список secong_num.
        main_num = list(zip(first_num,second_num)) # Из двух списков составляе список из нужных нам пар чисел.
print(main_num) # Выводим список пар чисел на экран.