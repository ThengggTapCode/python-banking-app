from packages import *

if __name__ == '__main__':
    jsonFileCheck()
    clearTerminal()
    
    signedIn = False
    signedInAs = ''
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
                clearTerminal()
                
                match choice:
                    # sign up
                    case '1':
                        signUpStatus, username = signUp()
                        signedIn = True if signUpStatus == 'sign_up_success' else False
                        signedInAs = username if signedIn else ''
                        sleepFor(1)
                        clearTerminal()
                        
                        match signUpStatus:
                            case 'sign_up_success':
                                print('Tạo tài khoản thành công!\n')
                            case 'username_existing':
                                print('Username đã tồn tại! Vui lòng nhập lại\n')
                        
                    # sign in
                    case '2':
                        signInStatus, username = signIn()
                        signedIn = True if signInStatus == 'sign_in_success' else False
                        signedInAs = username if signedIn else ''
                        sleepFor(1)
                        clearTerminal()
                        
                        match signInStatus:
                            # sign in success
                            case 'sign_in_success':
                                print('Đăng nhập thành công!\n')
                            # incorrect username
                            case 'incorrect_username':
                                print('Username không tồn tại! Vui lòng nhập lại\n')
                            # incorrect password
                            case 'incorrect_password':
                                print('Mật khẩu không đúng! Vui lòng nhập lại\n')
                            # no user available
                            case 'no_users_available':
                                print('Hiện tại không có tài khoản nào cả! Vui lòng tạo một tài khoản mới\n')
                    # exit
                    case '0':
                        pressAnyKeyToExit()
                        break
                    
                    # default
                    case _:
                        print('Vui lòng nhập lựa chọn hợp lệ\n')
            # force exit
            except KeyboardInterrupt:
                sleepFor(1)
                clearTerminal()
                forceExit()
                break

            sleepFor(1)
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
                clearTerminal()
                
                match choice:
                    # deposit
                    case '1':
                        deposit(signedInAs)
                    # exit
                    case '0':
                        pressAnyKeyToExit()
                        break
                    # any other features are n/a, please wait for updates!
            # force exit
            except KeyboardInterrupt:
                sleepFor(1)
                clearTerminal()
                forceExit()
                break
            sleepFor(1)