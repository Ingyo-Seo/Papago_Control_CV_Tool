import pystray # 시스템 트레이 모듈
import time # 시간 제어 모듈
import clipboard # 클립보드 제어 모듈
import pyautogui # 키보드 제어 모듈

import tkinter # GUI 모듈
import tkinter.font

from multiprocessing import Process, Queue

from PIL import Image

from pystray import MenuItem # 시스템 트레이 모듈

from selenium import webdriver # 크롤링 모듈
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from pynput.keyboard import Listener, Key, KeyCode # 입력감지 모듈

def quit_program():
    icon.stop()
    quit()

def start_papago():
    #pyautogui.hotkey("ctrl", "c")

    chrome_directory = Service("C:/Users/Seo/chromedriver.exe")

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("headless")

    driver = webdriver.Chrome(service = chrome_directory , options = chrome_options)

    driver.get("https://papago.naver.com/")

    time.sleep(2)

    original_text = clipboard.paste()

    false_localization = driver.find_element(By.ID,"sourceEditArea")
    button_localization = driver.find_element(By.ID,"btnTranslate")
    true_localization = driver.find_element(By.ID,"targetEditArea")

    false_localization.send_keys(original_text)

    button_localization.click()

    time.sleep(2)

    text_localization = true_localization.text

    clipboard.copy(text_localization)

    driver.quit()

    print("복사완료")

    #pyautogui.hotkey("ctrl", "v")

def test():
    print("test, test!!!")
 
def handleKeyPress( key ):
    if key in store:
        store.remove( key )
 
def handleKeyRelease( key ):
    store.add( key )
 
    for action, trigger in HOT_KEYS.items():
        CHECK = all([ True if triggerKey in store else False for triggerKey in trigger ])
 
        if CHECK:
            try:
                func = eval( action )
                if callable( func ):
                   func()
            except NameError as err:
                print( err )
        
    if key == Key.esc:
        return False

store = set()
 
HOT_KEYS = { "start_papago": set([ Key.ctrl_l, KeyCode(char="\x05")] ) }
 
with Listener(on_press=handleKeyPress, on_release=handleKeyRelease) as listener:
    listener.join()



icon.run()
