import pyautogui
import time
import json
import os
import keyboard  # Импортируем библиотеку keyboard

# Путь к файлу JSON
path = "items/cherniweva_Galina.json"

# Координаты для чекбоксов и текстовых полей
checkbox_coord = [(192, 396), (192, 519), (195, 642), (195, 766)]
text_area = [(339, 366), (314, 486), (380, 610), (241, 714)]

# Загрузка данных из JSON файла
with open(path, 'r', encoding='utf-8') as file:
    data = json.load(file)

def coord():
    print("Переместите курсор на нужное место через 5 секунд...")
    time.sleep(3)
    print(pyautogui.position())

def add_question():
    for i in range(len(data['questions'])):
        add_coordidates = [(100, 62), (967, 674), (249, 112)]
        time.sleep(3)

        # Кликаем по необходимым координатам
        for coords in add_coordidates:
            pyautogui.moveTo(coords[0], coords[1])
            pyautogui.click()

        time.sleep(0.5)  # Задержка между кликами
        question = data['questions'][i]
        
        # Вводим текст вопроса
        keyboard.write(question['question'], delay=0.1)

        # Обрабатываем варианты ответа
        for j, option in enumerate(question['options']):
            pyautogui.click(text_area[j])  # Клик по текстовому полю
            keyboard.write(option.replace('+', ''), delay=0.1)  # Вводим вариант ответа
            
            # Если вариант с '+', ставим галочку
            if '+' in option:
                pyautogui.click(checkbox_coord[j])
        
        # Кликаем по кнопке для завершения
        pyautogui.moveTo(251, 996)
        pyautogui.click()


# Добавляем вопросы
add_question()
# Основная часть программы
time.sleep(3)
pyautogui.moveTo(12, 33)
pyautogui.click()
pyautogui.moveTo(92, 135)
pyautogui.click()

# Записываем имя файла
keyboard.write(f'{os.path.basename(path)[:-5]}.mtf', delay=0.1)
pyautogui.moveTo(1757, 1002)
pyautogui.click()

