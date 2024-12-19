from .jsonFileHandling import *
from .common import *

def signIn():
    status = ''
    while True:
        users = readJsonFile()
        
        if len(users) == 0:
            status = 'no_users_available'
            return status
        
        # get input
        inputLine('Nhập username: ')
        username = input().lower()
        inputLine('Nhập mật khẩu: ')
        password = input().lower()
        
        for user in users:
            if user['username'] != username:
                status = 'incorrect_username'
            elif user['password'] != password:
                status = 'incorrect_password'
            else:
                status = 'sign_in_success'
                return status
        return status