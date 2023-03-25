import pyautogui as autochat

message = 'GudAfternoon'

if message:
    autochat.typewrite(message)
    autochat.press('enter')