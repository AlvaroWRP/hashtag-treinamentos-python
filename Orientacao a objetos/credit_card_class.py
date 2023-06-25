import random
from datetime import datetime


class CreditCard:
    def __init__(self, checking_account):
        self.owner = checking_account.person_name
        self.checking_account = checking_account
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
