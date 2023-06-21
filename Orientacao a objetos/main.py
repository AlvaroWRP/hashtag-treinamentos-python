from datetime import datetime

class CheckingAccount:
    """
    Checking account class for bank clients.

    Attributes:
        id (str): A person's ID.
        balance (int): The initial money after creating the account.
        transactions (list): All transactions made in an account.
    """

    def __init__(self, id):
        self.id = id
        self.balance = 0
        self.transactions = []


    @staticmethod
    def _get_current_date_and_time():
        """Gets the current time when a transaction is made.

        Returns:
            str: A string containing the date and time.
        """

        return datetime.now().strftime('%d/%m/%Y at %H:%M:%S')


    def _check_if_can_withdraw(self, money_to_withdraw):
        if self.balance - money_to_withdraw >= 0:
            return True

        return False


    def _log_transaction(self, transaction_type, value):
        value = float(f'{value:,.2f}')

        date_and_time = CheckingAccount._get_current_date_and_time()

        if transaction_type == 'deposit':
            self.transactions.append(('Deposit:', value, '| New balance:', self.check_balance(), '| Date:', date_and_time))

        elif transaction_type == 'withdraw':
            self.transactions.append(('Withdraw:', -value, '| New balance:', self.check_balance(), '| Date:', date_and_time))

        elif transaction_type == 'transference':
            self.transactions.append(('Transference:', -value, '| New balance:', self.check_balance(), '| Date:', date_and_time))

        elif transaction_type == 'receive':
            self.transactions.append(('Received:', value, '| New balance:', self.check_balance(), '| Date:', date_and_time))


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


    def transfer(self):
        money_to_transfer = float(input('\nHow much money do you want to transfer? '))

        permission_to_withdraw = self._check_if_can_withdraw(money_to_transfer)

        if permission_to_withdraw:
            self.balance -= money_to_transfer
            destination_account.balance += money_to_transfer
            print('\nTransference successful!\n')

            self._log_transaction('transference', money_to_transfer)
            destination_account._log_transaction('receive', money_to_transfer)


    def check_balance(self):
        return f'{self.balance:,.2f}'


    def show_transactions_log(self):
        print('\nTransactions log:\n')

        for log in self.transactions:
            print(*log)


my_account = CheckingAccount('12345')
destination_account = CheckingAccount('67890')

while True:
    print('Make a deposit - 1 | ' \
          'Withdraw cash - 2 | ' \
          'Check your balance - 3 | ' \
          'Transfer to another account - 4 | ' \
          'Finish - 5')

    user_choice = input('Choose an option: ')

    if user_choice == '1':
        my_account.deposit()

    elif user_choice == '2':
        my_account.withdraw()

    elif user_choice == '3':
        balance = my_account.check_balance()
        print(f'\nYour current balance is: ${balance}\n')

    elif user_choice == '4':
        my_account.transfer()

    elif user_choice == '5': break

    else: print('\nInvalid option.\n')

my_account.show_transactions_log()
destination_account.show_transactions_log()

# help(CheckingAccount)
# help(CheckingAccount._get_current_date_and_time)
