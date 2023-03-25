import pyautogui as autochat
import datetime
import time  # Возможно для задержки в отправлении сообщений пригодится
             # Для отправки разных сообщений в разное время, быть может for луп еще нужен.
             # может даже с внутренним циклом, для соотношений дат отправки с разным содержанием текста


# Вот тут вообще интуитивно
morning = datetime.datetime(year=2023, month=3, day=26, hour=8, minute=0, second=0, microsecond=0)
afternoon = datetime.datetime(year=2023, month=3, day=26, hour=14, minute=0, second=0, microsecond=0)
night = datetime.datetime(year=2023, month=3, day=26, hour=19, minute=0, second=0, microsecond=0)

if morning:
    message = 'GOOD MORNING'

    autochat.click()
    autochat.typewrite(message)
    autochat.press('enter')

elif afternoon:
    message = 'GOOD AFTERNOON'

    autochat.typewrite(message)
    autochat.press('enter')

elif night:
    message = 'GOOD NIGHT'

    autochat.typewrite(message)
    autochat.press('enter')
else:
    print('Incorrect data')