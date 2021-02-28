import os
import re
import shutil

# здесь название папки, в которую загружаем фото для сортировки. По умолчанию
# она находится в той же директории, где файл main.py

catalog = os.walk(r"photo-cat")


def sort_photo(catalog):
    folder = []
    date = []
    name = []
    a = 1
    # т.к os.walk создает генератор
    for i in catalog:
        folder.append(i)

    month_list = [0, 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
                  'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']

    for i in range(len(folder[0][2])):
        # С помощью регулярки получаем год/месяц/день из названия. Для каждого смартфона индивидуально
        year, month_num, day = re.findall(r'(\d\d\d\d)(\d\d)(\d\d)', folder[0][2][i])[0]
        # переводим цифру месяца в название
        month = month_list[int(month_num)]
        # Генерируем путь к новой папке
        new_dir = fr'F:\Cloud1\Фотки\{year}\\'
        path = os.path.join(new_dir)
        # Если такой папки нет, создаем
        if not os.path.exists(path):
            os.mkdir(path)
        new_dir = fr"F:\Cloud1\Фотки\{year}\{month_num} {month}\\"
        path = os.path.join(new_dir)
        if not os.path.exists(path):
            os.mkdir(path)
        # Сюда извлекается имя файла
        name.append(folder[0][2][i])
        shutil.move('photo-cat/' + name[i], new_dir)


sort_photo(catalog)