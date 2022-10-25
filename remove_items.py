import csv
import openpyxl


def css_reader():
    """
    Читаю csv файл со всеми товарами с магазина и результат записывает в список arr в виде массива
    :return: ничего
    """
    arr = []
    with open('Kaup24.ee_kaup.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            # row[0] = text + row[0]
            arr.append(row)
    print(arr)


def delete_row_from_css():
    """
    Нахождение по штртх-коду и удаление целой строки. Создание нового файла.
    :return: ничего
    """
    with open('Kaup24.ee_kaup.csv', 'r') as inp, open('Kaup24.ee_kaup_edit.csv', 'w', newline='') as out:
        writer = csv.writer(out)
        for row in csv.reader(inp):
            if row[4] != "6972401119183":
                writer.writerow(row)


def column_printout():
    """
    Вывод всех знчений одного столбца xlsx таблицы
    :return: ничего
    """
    path = "supplierProducts.xlsx"
    wb_obj = openpyxl.load_workbook(path)
    sheet_obj = wb_obj.active
    m_row = sheet_obj.max_row
    for i in range(1, m_row + 1):
        cell_obj = sheet_obj.cell(row=i, column=1)
        print(str(cell_obj.value))


def set_maker():
    """
    создает множество из штрихкодов всех товаров
    :return: ничего
    """
    dicts = {}
    arr = []
    with open('Kaup24.ee_kaup.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            arr.append(row)
        for i in arr:
            dicts[i[4]] = [i[0], i[1], i[2], i[3]]
    print(set(dicts.keys()))

# css_reader()
# delete_row_from_css()
# column_printout()
# set_maker()


path = "supplierProducts.xlsx"
wb_obj = openpyxl.load_workbook(path)
sheet_obj = wb_obj.active
m_row = sheet_obj.max_row
for i in range(1, m_row + 1):
    cell_obj = sheet_obj.cell(row=i, column=1)
    print(str(cell_obj.value))