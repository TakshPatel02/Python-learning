import pygetwindow as gw
import pyautogui
import time
import os

# For closing applications
def close_apps(app_name):
    for window in gw.getAllWindows():
        if app_name.lower() in window.title.lower():
            found = True
            window.activate()
            time.sleep(0.5)
            pyautogui.hotkey('ctrl' , 'w')
            print(f"Closed {window.title}")