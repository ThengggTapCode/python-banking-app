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
                sleepFor(1)
                
                match choice:
                    # sign up
                    case '1':
                        signUpStatus, username = signUp()
                        signedIn = True if signUpStatus == 'sign_up_success' else False
                        signedInAs = username if signedIn else ''
                        clearTerminal()
                        sleepFor(1)
                        
                        match signUpStatus:
                            # sign up success
                            case 'sign_up_success':
                                print('Tạo tài khoản thành công!\n')
                            # username existing
                            case 'username_existing':
                                print('Username đã tồn tại! Vui lòng nhập lại\n')
                            # confirm password not matching
                            case 'confirm_password_not_matching':
                                print('Vui lòng xác nhận lại mật khẩu!\n')
                            # if display name length is less than 1
                            case 'display_name_length_less_than_1':
                                print('Vui lòng nhập tên hiển thị từ 1 kí tự trở lên!\n')
                            # if username length is less than 1
                            case 'username_length_less_than_1':
                                print('Vui lòng nhập username từ 1 kí tự trở lên!\n')
                            # if password length is less than 1
                            case 'password_length_less_than_1':
                                print('Vui lòng nhập mật khẩu từ 1 kí tự trở lên!\n')
                        
                    # sign in
                    case '2':
                        signInStatus, username = signIn()
                        signedIn = True if signInStatus == 'sign_in_success' else False
                        signedInAs = username if signedIn else ''
                        clearTerminal()
                        sleepFor(1)
                        
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
                        clearTerminal()
                        break
                    
                    # default
                    case _:
                        print('Vui lòng nhập lựa chọn hợp lệ\n')
            # force exit
            except KeyboardInterrupt:
                clearTerminal()
                sleepFor(1)
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
                clearTerminal()
                sleepFor(1)
                
                match choice:
                    # deposit
                    case '1':
                        deposit(signedInAs)
                    # withdraw:
                    case '2':
                        withdraw(signedInAs)
                    # show balance
                    case '3':
                        showBalance(signedInAs)
                    # settings
                    case '4':
                        settingMenu()
                    # sign out
                    case '5':
                        status = signOut(signedInAs)
                        signedIn = False if status == 'sign_out_success' else True
                        
                        match status:
                            # incorrect password
                            case 'incorrect_password':
                                print('Mật khẩu không đúng! Hủy bỏ đăng xuất\n')
                            # sign out cancelled
                            case 'sign_out_cancelled':
                                print('Đã hủy bỏ đăng xuất\n')
                            # sign out success
                            case 'sign_out_success':
                                print('Đăng xuất thành công!\n')
                    # exit
                    case '0':
                        pressAnyKeyToExit()
                        clearTerminal()
                        break
                    # any other features are n/a, please wait for updates!
            # force exit
            except KeyboardInterrupt:
                clearTerminal()
                sleepFor(1)
                forceExit()
                clearTerminal()
                break
        sleepFor(1)