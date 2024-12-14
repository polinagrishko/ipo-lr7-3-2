import json # импорт модуля json для работы с json-файлами
# запрос у пользователя номера квалификации с преобразовванием его в целое число
number = int(input("Введите номер квалификации: "))
find = False # флаг, указывающий на то, найдена ли квалификация
with open("dump.json",'r',encoding = 'utf-8') as file: # открытие файла dump.json в режиме чтения
    data = json.load(file) # загрузка данных из файла в переменную data
    for skill in data: # цикл, проходящий по каждому элементу в перемнную data
        if skill.get("model") == "data.skill": # проверка, являетс ли введенное значение квалификацией (model = "data.skill")
            if skill["fields"].get("specialty") == number:#проверка, совпадает ли specialty текущей квалификации с введенным номером
                skill_code = skill["fields"].get("code")#если совпадает - получаем код квалификации
                skill_title = skill["fields"].get("title")#получаем название квалификации
                find = True # установка флага True если кваоификация найдена
for profession in data: # цикл для поиска информации о специальности
    if profession.get("model") == "data.specialty": # является ли текцщий элемент специальностью
        specialty_code = profession["fields"].get("code") # получение кода специальности 
        if specialty_code in skill_code: # содержится ли код специальности в коде квалификации
            specialty_title=profession["fields"].get("title") # получение названия специальности
            specialty_educational = profession["fields"].get("c_type") # получение типа образования специальности
if not find: # проверка флага find, если find=False: вывод сообщения 
    print("=============== Не Найдено ===============")
else: # если флаг True, вывод соответствующих сообщенйи
    print("=============== Найдено ===============")
    print(f"{specialty_code} >> Специальность '{specialty_title}', {specialty_educational}")
    print(f"{skill_code} >> Квалификация '{skill_title}'")