def open_account():
    print("새 계좌 생성.")
    

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원".format(balance + money))
    return balance + money

balance = 0
balance = deposit(balance, 1000)
print(balance)