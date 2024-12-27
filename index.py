import json

def display_all_records(data): #функция для вывода всех записей
    print("===========")
    for sity in data: #перебирает все записи и выводит на экран
        print(f'{sity["id"]}: {sity["name"]}, {sity["country"]}\nНаселение: {sity["people_count"]}, >100000 ?: {sity["is_big"]}\n==========')

def display_one_record(data): #вывод одной записи
    k = 0 #переменная для номера записи
    flag = True #флаг для запоминания, найдена запись или нет
    inp_id = input("Введите поле выводимой записи: ")
    if inp_id.isdigit():
        inp_ip = int(inp_id)
    else:
        print("Некорректный ввод\n")
        return 0
    for sity in data: #цикл с поиском по всем записей
        k += 1
        if inp_id == sity["id"]:
            print(f'{sity["id"]}: {sity["name"]}, {sity["country"]}\nНаселение: {sity["people_count"]}, >100000 ?: {sity["is_big"]}\nПорядковый номер записи: {k}\n==========')
            flag = False
    print("=====Запись не найдена======\n" if flag else "")

def new_record(data): #функция для создания записи
    new_sity = {"id":0, "name":"", "country":"", "is_big":False,"people_count":0} #множество для добавляемой записи
    new_sity["id"] = data[-1]["id"] + 1
    new_sity["name"] = input("Введите название города: ")
    new_sity["country"] = input("Введите страну: ")
    try:
        new_sity["people_count"] = int(input("Введите население: "))
    except:
        print("Некорректное значение\n")
    new_sity["is_big"] = (True if new_sity["people_count"]>100000 else False)
    data.append(new_sity) #множество записывается в data

def delete_record(data):#функция для удаления записи
    k = 0#переменная для номера записи
    flag = True#флаг для запоминания, найдена запись или нет
    inp_id = input("Введите поле удаляемой записи: ")
    if inp_id.isdigit():
        inp_ip = int(inp_id)
    else:
        print("Некорректный ввод\n")
        return 0
    for sity in data: #цикл с поиском нужной записи и удалением её из data
        if inp_id == sity["id"]:
            data.pop(k)
            flag = False
        k += 1
    print("=====Запись не найдена======\n" if flag else "")

def closing_prog(data, num_op): #функция закрытия проги и перенос data в файл k.json
    print(f'Завершение работы программы. Было выполнено {num_op} действий')
    with open('k.json', 'w', encoding='utf-8') as file: #информация записывается обратно в файл
        json.dump(data, file, indent=4, ensure_ascii=True)
    exit()

def menu(data, num_op): #функция "меню"
    print("1 - Вывести все записи\n2 - Вывести запись по полю\n3 - Добавить запись\n4 - Удалить запись по полю\n5 - Выйти из программы\n")
    c = int(input("Выберите действие(введите число): ")) #запрашивает действие пользователя в переменную
    
    if c == 1: #выводит все записи
        display_all_records(data)

    elif c == 2:#выводит поле записи, id которой ввел пользователь
        display_one_record(data)
    
    elif c == 3: #ввод всех данных, запись их в множество и добавление множество в data
        new_record(data)
        
    elif c == 4: #находится id в файле, после чего запись с нужным id удаляется
        delete_record(data)
    
    elif c == 5: #завершается цикл
        closing_prog(data, num_op)
        
    else: #при вводе некорректного значения
        print('Введите корректное значение')

def main(): #главная функция
    num_op = 0
    with open('k.json', 'r', encoding='utf-8') as file: #открывается файл json и записывается в data
        data = json.load(file)
        while True: #цикл повторяется постоянно
            menu(data, num_op) #запускается функция "меню"
            num_op += 1
main() #запуск главной функции