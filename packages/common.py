import os
import time

def clearTerminal():
    clear = 'cls' if os.name == 'nt' else 'clear'
    return os.system(clear)

def forceExit():
    input('Đã bấm Ctrl-C để thoát khẩn cấp - Bấm bất kì phím nào để thoát...\n')
    
def pressAnyKeyToExit():
    input('Nhập bất kì phím nào để thoát...\n')

def inputLine(msg):
    print(f'{msg}\n>', end=' ')

def sleepFor(seconds):
    return time.sleep(seconds)

def formatNumber(num):
    return f'{num:,.2f}'.replace(',', 'X').replace('.',',').replace('X', '.')