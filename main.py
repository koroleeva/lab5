import random


def task1():
    list = [2, 4, 8, 9, 3]
    a = int(input("Угадай число"))
    if a in list:
        print(list, "Ваше число:", a, " Поздравляю, Вы угадали число!")
    else:
        print(list, "Ваше число:", a, " Нет такого числа")


def task2():
    list1 = [1, 3, 2, 4, 3, 7, 6, 5, 7, 1, 9, 3]
    list2 =[]
    for item in list1:
        if list1.count(item) >= 2:
            list2.append(item)
    list3 = list(set(list2))
    print(*list3)


def task3():
    tuple1 = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
    a = int(input("Сколько выходных вы хотите?"))
    b = 7-a
    print("Ваши выходные дни:", *tuple1[7-a:8])
    print("Ваши рабочие дни:", *tuple1[0:b])


def task4():
    list1 = ["Егорова", "Иванов", "Рукин", "Королева", "Панченко", "Веренин", "Абрамова", "Юзвов", "Кусенков", "Майер"]
    list2 = ["Сидоров", "Петров", "Иванов", "Козлова", "Сергеева", "Воронин", "Баталова", "Семенов", "Григорьев", "Жукова"]
    tuplesport = tuple(sorted(random.sample(list1, 5)+random.sample(list2, 5)))
    print('Фамилии студентов первой группы:', *list1)
    print('Фамилии студентов второй группы:', *list2)
    print('Спортивная команда:', *tuplesport)
    print('Количество человек спортивной команды:', len(tuplesport))
    n = 0
    for item in tuplesport:
        if (item == "Иванов"):
            n = n + 1
        else:
            n = n + 0
    print('Студент с фамилией Иванов встречается в команде ', n, " раз(а)")


task1()
task2()
task3()
task4()