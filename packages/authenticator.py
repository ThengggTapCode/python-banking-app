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
    
    for user in users:
        if user['username'] == username:
            # if username and password matches then sign in success
            if user['password'] == password:
                return 'sign_in_success', username
            # if password didnt match
            else:
                return 'incorrect_password', None
    # if username didnt match
    return 'incorrect_username', None