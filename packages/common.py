import os
import keyboard
import time

def clearTerminal():
    return os.system('cls')

def forceExit():
    print('Đã bấm Ctrl-C để thoát khẩn cấp - Bấm bất kì phím nào để thoát')
    keyboard.read_event()
    
def pressAnyKeyToExit():
    print('Nhập bất kì phím nào để thoát...')
    keyboard.read_event()

def inputLine(msg):
    print(f'{msg}\n>', end=' ')

def sleepFor(seconds):
    return time.sleep(seconds)