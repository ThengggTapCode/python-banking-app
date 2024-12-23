from .common import *
from .jsonFileHandling import *
from .authenticator import passwordChecking
  
def settingMenu():
    while True:
        print('1. Đổi tên hiển thị')
        print('2. Đổi username')
        print('3. Đổi mật khẩu')
        print('0. Thoát')
        
        inputLine('Nhập lựa chọn của bạn')
        choice = input()
        clearTerminal()
        sleepFor(1)
        
        match choice:
            # change display name
            case '1':
                pass
            # change username
            case '2':
                pass
            # change password:
            case '3':
                pass
            # exit
            case '0':
                break
