# Задача 1. Дан список элементов. Используя библиотеку NumPy, 
# подсчитайте количество уникальных элементов в нём.

import numpy as np

def Task1():
    elements = [1, 2, 3, 4, 5, 1, 2, 3]
    arr = np.array(elements)
    unique_elements, counts = np.unique(arr, return_counts=True)
    print("Уникальные элементы:", unique_elements)
    print("Количество уникальных элементов:", len(unique_elements))
Task1()

# Задача 2. Создайте двумерный массив, размером 5х5. 
# Определите, есть ли в нём одинаковые строки.

def Task2():
    array = np.array([
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [1, 2, 3, 4, 5],
        [16, 17, 18, 19, 20]
    ])
    has_duplicate_rows = False
    unique_rows, row_counts = np.unique(array, axis=0, return_counts=True)
    duplicates = unique_rows[row_counts > 1]

    if len(duplicates) > 0:
        has_duplicate_rows = True

    if has_duplicate_rows:
        print("В массиве есть одинаковые строки.")
    else:
        print("В массиве нет одинаковых строк.")
Task2()

# Задача 3. Создайте двумерный массив случайного размера. 
# Найдите индексы максимального и минимального элементов в нём.
# Выведите элементы главной диагонали матрицы в виде одномерного массива.

def Task3():
    rows = np.random.randint(2, 6)  
    cols = np.random.randint(2, 6)  
    array = np.random.randint(0, 10, size=(rows, cols))  

    max_index = np.unravel_index(np.argmax(array), array.shape)
    min_index = np.unravel_index(np.argmin(array), array.shape)

    print("Индекс максимального элемента:", max_index)
    print("Индекс минимального элемента:", min_index)

    diagonal_elements = np.diag(array)
    print("Элементы главной диагонали:", diagonal_elements)
Task3()