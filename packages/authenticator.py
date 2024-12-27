from .jsonFileHandling import *
from .common import *

def signUp():
    users = readJsonFile()
    # get input
    inputLine('Nhập tên hiển thị')
    displayName = input().strip()
    
    inputLine('Nhập username mới')
    username = input().lower().strip()
    
    inputLine('Nhập mật khẩu mới')
    password = input().lower().strip()
    
    inputLine('Xác nhận lại mật khẩu')
    confirmPassword = input().lower().strip()
    
    # if display name length is less than 1
    if not checkInfoLength(displayName):
        return 'display_name_length_less_than_1', None
    # if username length is less than 1
    if not checkInfoLength(username):
        return 'username_length_less_than_1', None
    # if password length is less than 1
    if not checkInfoLength(password):
        return 'password_length_less_than_1', None
    
    sleepFor(1)
    for user in users:
        # exit if username existing
        if user['username'] == username:
            return 'username_existing', None
    # exit if confirm password not matching
    if confirmPassword != password:
        return 'confirm_password_not_matching', None
    
    # add user data to json file
    users.append({
        "displayName": displayName,
        "username": username,
        "password": password,
        "balance": 0.0
    })
    saveDataToJson(users)
    return 'sign_up_success', username
        
def signIn():
    users = readJsonFile()
    
    if len(users) == 0:
        return 'no_users_available', None
    
    # get input
    inputLine('Nhập username: ')
    username = input().lower().strip()
    
    inputLine('Nhập mật khẩu: ')
    password = input().lower().strip()
    
    passwordStatus = passwordChecking(username, password)
    
    match passwordStatus:
        case 'password_matching':
            return 'sign_in_success', username
        case 'username_not_found':
            return 'incorrect_username', None
        case 'incorrect_password':
            return passwordStatus, None
    

def signOut(username):
    while True:
        # get confirm input
        inputLine('Bạn có chắc muốn đăng xuất tài khoản không? Nhập Y/y để đồng ý, N/n để hủy')
        choice = input().lower().strip()
        clearTerminal()
        sleepFor(1)
        
        if choice == 'n':
            # cancel sign out
            clearTerminal()
            return 'sign_out_cancelled'
        if choice == 'y':
            # exit loop to get password
            break
        else:
            # print then wait for 1 sec
            print('Vui lòng nhập lựa chọn hợp lệ!\n')
            sleepFor(1)
    
    # get input password
    inputLine('Nhập lại mật khẩu để xác nhận đăng xuất tài khoản')
    password = input().lower().strip()
    clearTerminal()
    sleepFor(1)
    
    # get password status
    passwordStatus = passwordChecking(username, password)
    return 'sign_out_success' if passwordStatus == 'password_matching' else 'incorrect_password'
        
def passwordChecking(username, password):
    # get 'users' array from json file
    users = readJsonFile()
    
    for user in users:
        if user['username'] == username:
            # if matching password
            if user['password'] == password:
                return 'password_matching'
            # else
            return 'incorrect_password'
    # if username not found
    return 'username_not_found'

def checkInfoLength(info):
    return True if len(info) > 0 else False