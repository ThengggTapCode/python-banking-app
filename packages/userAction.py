from .common import *
from .jsonFileHandling import updateJsonData, readJsonFile

def deposit(username):
    users = readJsonFile()
    
    for user in users:
        if user['username'] == username:
            # get input
            while True:
                try:
                    inputLine('Nhập số tiền cần nạp')
                    ammount = float(input())
                    clearTerminal()
                    sleepFor(1)
                    
                    if ammount < 1:
                        print('Vui lòng nhập số tiền lớn hơn 0\n')
                    else:
                        currentBalance = user['balance']
                        newBalance = currentBalance + ammount
                        updateJsonData({'balance': newBalance}, username)
                        print(f'Đã nạp thành công {formatNumber(ammount)}vnđ! Hiện đang có {formatNumber(newBalance)}vnđ trong tài khoản\n')
                        sleepFor(1)
                        break
                    
                except ValueError:
                    print('Vui lòng nhập số!\n')
