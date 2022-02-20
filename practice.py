def open_account():
    print("새 계좌 생성.")
    

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("출금 완료")
    else: 
        print("출금 실패")

balance = 0
balance = deposit(balance, 1000)
print(balance)
withdraw(1000, 500)