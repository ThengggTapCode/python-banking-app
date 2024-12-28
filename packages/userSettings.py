from .common import *
from .jsonFileHandling import *
from .authenticator import passwordConfirm
        
def changeDisplayName(username):
    # get new display name
    inputLine('Nhập tên hiển thị mới')
    displayName = input().strip()
    
    # if display name length is less than 1
    if len(displayName) == 0:
        return 'display_name_length_less_than_1'
    
    # update json file
    updateJsonData({'displayName': displayName}, username)
    return 'changed_display_name'

def changeUsername(username):
    # get password status from input
    passwordStatus = passwordConfirm(username, 'Nhập lại mật khẩu để xác nhận đổi username')
    
    match passwordStatus:
        # ussername not found
        case 'username_not_found':
            return passwordStatus
        # incorrect password
        case 'incorrect_password':
            return passwordStatus
        # matching password
        case 'password_matching':
            # get new ussername
            inputLine('Nhập username mới')
            newUsername = input().lower().strip()
            
            # get confirm username
            inputLine('Xác nhận lại username mới')
            confirmUsername = input().lower().strip()
            
            # if username length is less than 1
            if len(newUsername) == 0:
                return 'new_username_length_less_than_1'
            # if confirm username not matching
            if confirmUsername != newUsername:
                return 'confirm_username_not_matching'

            # update json file
            updateJsonData({'username': newUsername}, username)
            return 'changed_username'
        
def changePassword(username):
    # get password status from input
    passwordStatus = passwordConfirm(username, 'Nhập lại mật khẩu để xác nhận đổi mật khẩu')
    
    match passwordStatus:
        # ussername not found
        case 'username_not_found':
            return passwordStatus
        # incorrect password
        case 'incorrect_password':
            return passwordStatus
        # matching password
        case 'password_matching':
            # get new password
            inputLine('Nhập mật khẩu mới')
            newPassword = input().lower().strip()
            
            # get confirm pasdword
            inputLine('Xác nhận lại mật khẩu mới')
            confitmPassword = input().lower().strip()
            
            # if password length is less than 1
            if len(newPassword) == 0:
                return 'new_password_length_less_than_1'
            # if confimt password not matching
            if confitmPassword != newPassword:
                return 'confirm_password_not_matching'

            # update json file
            updateJsonData({'password': newPassword}, username)
            return 'changed_password'
            
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
