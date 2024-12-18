import os
import keyboard

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
    
def main():
    signedIn = False
    
    while True:
        if not signedIn:
            # print menu
            print('1. Đăng kí tài khoản')
            print('2. Đăng nhập')
            print('0. Thoát\n')
            
            try:
                # get user input
                inputLine('Nhập lựa chọn của bạn')
                choice = input()

                match choice:
                    # sign up
                    case '1':
                        print('sign-up')
                        
                    # sign in
                    case '2':
                        print('sign-in')
                    
                    # exit
                    case '0':
                        pressAnyKeyToExit()
                        break
            # force exit
            except KeyboardInterrupt:
                forceExit()
                break
            
        else:
            # print option
            print('1. Nạp tiền')
            print('2. Rút tiền')
            print('3. Xem số dư')
            print('4. Cài đặt')
            print('5. Đăng xuất')
            print('0. Thoát\n')
            
            try:
                # get user input
                inputLine('Nhập lựa chọn của bạn')
                choice = input()
                
                match choice:
                    # exit
                    case '0':
                        pressAnyKeyToExit()
                        break
                    
            except KeyboardInterrupt:
                forceExit()
                break
            
if __name__ == '__main__':
    clearTerminal()
    main()