from .common import *
from .jsonFileHandling import updateJsonData, readJsonFile

def deposit(username):
    # get 'users' array from json
    users = readJsonFile()
    
    for user in users:
        # if matching username
        if user['username'] == username:
            # get input
            while True:
                try:
                    # get input
                    inputLine('Nhập số tiền cần nạp')
                    ammount = float(input())
                    clearTerminal()
                    sleepFor(1)
                    
                    # add ammount to current balance
                    currentBalance = user['balance']
                    newBalance = currentBalance + ammount
                    
                    # update user balance
                    updateJsonData({'balance': newBalance}, username)
                    print(f'Đã nạp thành công {formatNumber(ammount)}vnđ! Hiện đang có {formatNumber(newBalance)}vnđ trong tài khoản\n')
                    
                    return
                
                # if ammount is not number
                except ValueError:
                    print('Vui lòng nhập số!\n')

def withdraw(username):
    # get 'users' array from json
    users = readJsonFile()
    
    for user in users:
        # if matching username
        if user['username'] == username:
            # exit if current balance is 0
            currentBalance = user['balance']
            if currentBalance < 1:
                return
            
            while True:
                try:
                    # get input
                    inputLine('Nhập số tiền cần rút')
                    ammount = float(input())
                    clearTerminal()
                    sleepFor(1)

                    # print if ammount is greater than current balance
                    if ammount > currentBalance:
                        print(f'Số dư không đủ để rút! Vui lòng nhập số tiền không quá {formatNumber(currentBalance)}vnđ!\n')
                    else:
                        # subtract ammount from current balance
                        newBalance = currentBalance - ammount
                        
                        # update user balance
                        updateJsonData({'balance': newBalance}, username)
                        print(f'Đã rút thành công {formatNumber(ammount)}vnđ! Hiện đang có {formatNumber(newBalance)}vnđ trong tài khoản\n')
                        
                        return
                # if ammount is not a number
                except ValueError:
                    print('Vui lòng nhập số!\n')
                    
def showBalance(username):
    # get 'users' array from json
    users = readJsonFile()
    
    for user in users:
        # if matching username
        if user['username'] == username:
            # wait for 1 sec
            currentBalance = user['balance']
            print(f'Hiện đang có {formatNumber(currentBalance)}vnđ trong tài khoản\n')