import matching
import time
import pyperclip
import pyautogui as pg
#you have to design Subject email to make sense with your bot
def check_work():
    matching.BOT('subject1.JPG')
    time.sleep(2)
    matching.BOT('reply.JPG')

    text = '''
    Please wait a minute we will do as soon as possible!!!
    '''

    pyperclip.copy(text)
    time.sleep(3)
    pg.hotkey('ctrl','v')
    time.sleep(3)
    matching.BOT('send.JPG')
    time.sleep(3)
    matching.BOT('back.JPG')
    time.sleep(3)
    pg.moveTo(500,500)
    pg.scroll(-100)

for i in range(2) :
    check_work()