from .jsonFileHandling import *
from .common import *

def signUp():
    status = ''
    while True:
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
            if user['username'] == username:
                status = 'username_existing'
                return status
            
        users.append({
            "displayName": displayName,
            "username": username,
            "password": password
        })
        saveDataToJson(users)
        status = 'sign_up_success'
        return status
        
def signIn():
    status = ''
    while True:
        users = readJsonFile()
        
        if len(users) == 0:
            status = 'no_users_available'
            return status
        
        # get input
        inputLine('Nhập username: ')
        username = input().lower().strip()
        
        inputLine('Nhập mật khẩu: ')
        password = input().lower().strip()
        
        for user in users:
            if user['username'] != username:
                status = 'incorrect_username'
            elif user['password'] != password:
                status = 'incorrect_password'
            else:
                status = 'sign_in_success'
                return status
        return status