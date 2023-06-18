from datetime import datetime

class CheckingAccount:
    def __init__(self, name, cpf):
        self.name = name
        self.cpf = cpf
        self.balance = 0
        self.transactions = []

    
    @staticmethod
    def _get_current_date_and_time():
        return datetime.now().strftime('%d/%m/%Y at %H:%M:%S')


    def _check_if_can_withdraw(self, money_to_withdraw):
        if self.balance - money_to_withdraw >= 0:
            return True
        
        return False


    def _log_transaction(self, transaction_type, value):
        date_and_time = self._get_current_date_and_time()

        if transaction_type == 'deposit':
            self.transactions.append(('Deposit:', value, '| New balance:', self.check_balance(), '| In:', date_and_time))

        elif transaction_type == 'withdraw':
            self.transactions.append(('Withdraw:', -value, '| New balance:', self.check_balance(), '| In:', date_and_time))


    def deposit(self):
        money_to_deposit = float(input('\nHow much money do you want to deposit? '))

        self.balance += money_to_deposit
        print('\nTransaction successful!\n')

        self._log_transaction('deposit', money_to_deposit)


    def withdraw(self):
        money_to_withdraw = float(input('\nHow much money do you want to withdraw? '))

        permission_to_withdraw = self._check_if_can_withdraw(money_to_withdraw)

        if permission_to_withdraw:
            self.balance -= money_to_withdraw
            print('\nWithdraw successful!\n')

            self._log_transaction('withdraw', money_to_withdraw)

        else: print('\nYou do not have enough money.\n')


    def check_balance(self):
        return f'{self.balance:,.2f}'


    def show_transactions_log(self):
        print('\nTransactions log:\n')

        for log in self.transactions:
            print(*log)


account_1 = CheckingAccount('Álvaro', '123.456.789-00')

while True:
    print('Make a deposit - 1 | Withdraw cash - 2 | Check your balance - 3 | Finish - 4')

    user_choice = input('Choose an option: ')

    if user_choice == '1':
        account_1.deposit()

    elif user_choice == '2':
        account_1.withdraw()

    elif user_choice == '3':
        balance = account_1.check_balance()
        print(f'\nYour current balance is: ${balance}\n')
    
    elif user_choice == '4': break
    
    else: print('\nInvalid option.\n')

account_1.show_transactions_log()
