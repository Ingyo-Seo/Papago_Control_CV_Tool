import pystray # 시스템 트레이 모듈
import time # 시간 제어 모듈
import clipboard # 클립보드 제어 모듈
import pyautogui # 키보드 제어 모듈

import tkinter # GUI 모듈
import tkinter.font

from PIL import Image

from pystray import MenuItem # 시스템 트레이 모듈

from selenium import webdriver # 크롤링 모듈
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from pynput.keyboard import Listener, Key, KeyCode # 입력감지 모듈
 
store = set()
 
HOT_KEYS = { "start_papago2": set([ Key.ctrl_l, KeyCode(char="\x05")] ) }
 
def info_program():
    window = tkinter.Tk()
    
    window.title("파파고 복붙툴 정보")
    window.geometry("500x100")
    window.resizable(False, False)

    font=tkinter.font.Font(family="맑은 고딕", size=10, slant="italic")

    label = tkinter.Label(window, text="Ctrl + E 키를 입력하면 약 4초뒤에 파파고로 문자를 번역하여 바꿔줍니다.", font=font, pady=50)
    label.place(y=50)
    label.pack()
    
    window.mainloop()

def quit_program():
    quit()

def start_papago2():
    print("test")

def start_papago():
    pyautogui.hotkey("ctrl", "c")

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

    pyautogui.hotkey("ctrl", "v")
 
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

        
    # 종료
    if key == Key.esc:
        return False
 
with Listener(on_press=handleKeyPress, on_release=handleKeyRelease) as listener:
    listener.join()
