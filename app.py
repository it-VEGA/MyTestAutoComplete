import pyautogui
import time
import json
import os

path = "items/english.json"

checkbox_coord = [(192,396),(192,519),(195,642),(195,766)]
text_area = [(339,366),(314,486),(380,610),(251,996)]
with open(path, 'r', encoding='utf-8') as file:
    data = json.load(file)
    print(len(data['questions']))

def coord():
    print("Переместите курсор на нужное место через 5 секунд...")
    time.sleep(3)
    print(pyautogui.position())

def add_question():
    for i in range(0,len(data['questions'])):
        add_coordidates = [(100,62),(967,674), (249,112)]
        time.sleep(3)
        for coords in add_coordidates:
            pyautogui.moveTo(coords[0], coords[1])
            pyautogui.click()
        time.sleep(0.5)  # Задержка между кликами
        question = data['questions'][i]
        pyautogui.typewrite(question['question'])
        for i,option in enumerate(question['options']):
            pyautogui.click(text_area[i])
            pyautogui.write(option.replace('+', ''))
            if '+' in option:
                pyautogui.click(checkbox_coord[i])
        pyautogui.moveTo(251,996)
        pyautogui.click()
time.sleep(3)
pyautogui.moveTo(12,33)
pyautogui.click()
pyautogui.moveTo(92,135)
pyautogui.click()

pyautogui.write(f'{os.path.basename(path)[-4:]}.mtf')
pyautogui.moveTo(1757,1002)
pyautogui.click()

coord()
# add_question()