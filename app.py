import pyautogui
import time
import json

checkbox_coord = [(192,396),(192,519),(195,642),(195,766)]
text_area = [(339,366),(314,486),(380,610),(251,996)]
with open('items/english.json', 'r', encoding='utf-8') as file:
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

# coord()
add_question()

        # pyautogui.moveTo(339,366)
        # pyautogui.click()
        # pyautogui.typewrite(question['options'][0].replace('+',''))
        # pyautogui.moveTo(314,486)
        # pyautogui.click()
        # pyautogui.typewrite(question['options'][1])
        # pyautogui.moveTo(380,610)
        # pyautogui.click()
        # pyautogui.typewrite(question['options'][2])