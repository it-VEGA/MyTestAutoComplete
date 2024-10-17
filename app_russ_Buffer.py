import pyautogui
import time
import json
import os
import pyperclip

path = "items/Diana 11 class.json"

checkbox_coord = [(192,396),(192,519),(195,642),(195,766),(191,882)]
text_area = [(339,366),(314,486),(380,610),(241, 714),(342,858)]
with open(path, 'r', encoding='utf-8') as file:
    data = json.load(file)

def paste_text(text):
    pyperclip.copy(text)  # Копируем текст в буфер обмена
    pyautogui.hotkey('ctrl', 'v')  # Вставляем текст с помощью Ctrl + V

def add_question():
    for i in range(0,len(data['questions'])):
        add_coordidates = [(100,62),(967,674), (249,112)]
        time.sleep(2)
        for coords in add_coordidates:
            pyautogui.moveTo(coords[0], coords[1])
            pyautogui.click()
        time.sleep(0.5)  # Задержка между кликами
        question = data['questions'][i]
        paste_text(question['question'])  # Используем вставку текста вместо ввода
        for i, option in enumerate(question['options']):
            pyautogui.click(text_area[i])
            paste_text(option.replace('+', ''))  # Вставляем текст ответа
            if '+' in option:
                pyautogui.click(checkbox_coord[i])
        pyautogui.moveTo(251,996)
        pyautogui.click()


add_question()
time.sleep(1)
pyautogui.moveTo(12,33)
pyautogui.click()
pyautogui.moveTo(92,135)
pyautogui.click()

pyautogui.write(f'{os.path.basename(path)[:-5]}.mtf')
pyautogui.moveTo(1757,1002)
pyautogui.click()
