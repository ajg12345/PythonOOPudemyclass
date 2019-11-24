#!/home/aaron4udemy/anaconda3/envs/udem/bin/python
from random import randint

class SAccount():
    def __init__(self, name, deposit, acctNumber):
        self.name = name
        self.total = float(deposit)
        self.acctNumber = acctNumber
        print('your acctNumber is ',str(self.acctNumber))
    def withdraw(self, amount):
        if self.total >= float(amount):
            self.total -= float(amount)
            print('you have deducted ' + str(amount) + ' from your account. ' +  str(self.total) + ' remaining.')
        else:
            print('you do not have enough money for that amount, please try again')
    
    def getBalance(self):
        print(str(self.total))

    def deposit(self, amount):
        self.total += float(amount)
        print(str(amount) + ' has been depositet. '+str(self.total) + ' is the new balance ')

while True:
    print('would you like to make a "NEW" s account or access "EXISTING" one? (press x to quit)')
    resp = input()
    if resp == 'x':
        quit()
    elif resp == "NEW":
        print()
        print('please enter your name')
        name = input()
        print('please enter your initial deposit')
        deposit = float(input())

        account = SAccount(name, deposit, randint(10000,99999))
    elif resp == "EXISTING":
        print()
        print('please enter your acct number')
        acctNumber = input()
        print('please enter your name')
        name = input()
        if account.name == name and acctNumber == str(account.acctNumber):
            while True:
                print('you have accessed your account, press w for withdraw, d for deposit, b for balance, or l to logout')
                resp = input()
                if resp == 'l':
                    break
                if resp == 'b':
                    account.getBalance()
                else:
                    print('please enter an amount')
                    amount = input()
                    if resp == 'w':                    
                        account.withdraw(amount)
                    if resp == 'd':
                        account.deposit(amount)


