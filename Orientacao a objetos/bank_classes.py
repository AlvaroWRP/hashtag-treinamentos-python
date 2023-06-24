from datetime import datetime
import random

class CheckingAccount:
    """
    Checking account class for bank clients.

    Attributes:
        person_id (str): A person's ID.
        agency (str): The agency number.
        account_number (str): The account's unique number.
        _balance (int): The initial money after creating the account.
        _transactions (list): All transactions made in an account.
        credit_cards (list): All credit cards linked to an account.
    """

    def __init__(self, person_id, agency, account_number):
        self.person_id = person_id
        self.agency = agency
        self.account_number = account_number
        self._balance = 0
        self._transactions = []
        self.credit_cards = []


    @staticmethod
    def _get_current_date_and_time():
        """Gets the current time when a transaction is made.

        Returns:
            str: A string containing the date and time.
        """

        return datetime.now().strftime('%d/%m/%Y at %H:%M:%S')


    def _check_if_can_withdraw(self, money_to_withdraw):
        if self._balance - money_to_withdraw >= 0:
            return True

        return False


    def _log_transaction(self, transaction_type, value):
        value = float(f'{value:,.2f}')

        date_and_time = CheckingAccount._get_current_date_and_time()

        if transaction_type == 'deposit':
            self._transactions.append(('Deposit:', value, '| New balance:', self.check_balance(), '| Date:', date_and_time))

        elif transaction_type == 'withdraw':
            self._transactions.append(('Withdraw:', -value, '| New balance:', self.check_balance(), '| Date:', date_and_time))

        elif transaction_type == 'transference':
            self._transactions.append(('Transference:', -value, '| New balance:', self.check_balance(), '| Date:', date_and_time))

        elif transaction_type == 'receive':
            self._transactions.append(('Received:', value, '| New balance:', self.check_balance(), '| Date:', date_and_time))


    def deposit(self):
        money_to_deposit = float(input('\nHow much money do you want to deposit? '))

        self._balance += money_to_deposit
        print('\nTransaction successful!\n')

        self._log_transaction('deposit', money_to_deposit)


    def withdraw(self):
        money_to_withdraw = float(input('\nHow much money do you want to withdraw? '))

        permission_to_withdraw = self._check_if_can_withdraw(money_to_withdraw)

        if permission_to_withdraw:
            self._balance -= money_to_withdraw
            print('\nWithdraw successful!\n')

            self._log_transaction('withdraw', money_to_withdraw)

        else: print('\nYou do not have enough money.\n')


    def transfer(self, destination_account):
        money_to_transfer = float(input('\nHow much money do you want to transfer? '))

        permission_to_withdraw = self._check_if_can_withdraw(money_to_transfer)

        if permission_to_withdraw:
            self._balance -= money_to_transfer
            destination_account._balance += money_to_transfer
            print('\nTransference successful!\n')

            self._log_transaction('transference', money_to_transfer)
            destination_account._log_transaction('receive', money_to_transfer)


    def check_balance(self):
        return f'{self._balance:,.2f}'


    def show_transactions_log(self):
        print('\nTransactions log:\n')

        for log in self._transactions:
            print(*log)


    def show_credit_cards(self):
        print('\nYour credit cards:\n')

        for credit_card in self.credit_cards:
            for info in credit_card.items():
                print(info)

            print()


class CreditCard:
    def __init__(self, owner, checking_account):
        self.owner = owner
        self.checking_account = checking_account
        self._limit = 5_000
        self._password = '1234'
        self.cvv = CreditCard._generate_cvv()  # Card Verification Value
        self.number = CreditCard._generate_number()
        self.expiration_date = CreditCard._generate_expiration_date()

        checking_account.credit_cards.append(self.__dict__)


    @staticmethod
    def _generate_number():
        random_number = str(random.randint(1000_0000_0000_0000, 9999_9999_9999_9999))

        first_section = random_number[:4]
        second_section = random_number[4:8]
        third_section = random_number[8:12]
        fourth_section = random_number[12:]

        return f'{first_section} {second_section} {third_section} {fourth_section}'


    @staticmethod
    def _generate_expiration_date():
        month = datetime.now().month
        year = datetime.now().year + 8

        return datetime(year, month, 1).strftime('%m/%y')


    @staticmethod
    def _generate_cvv():
        first_digit = random.randint(0, 9)
        second_digit = random.randint(0, 9)
        third_digit = random.randint(0, 9)

        return f'{first_digit}{second_digit}{third_digit}'


    @property
    def password(self):
        return self._password


    @password.setter
    def password(self, new_password):
        if len(new_password) == 4 and new_password.isdigit():
            self._password = new_password
            print('Password changed!')

        else:
            print('Not a valid password.')
