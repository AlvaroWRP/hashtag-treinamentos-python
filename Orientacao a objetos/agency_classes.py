from datetime import datetime


class Agency:
    def __init__(self, checking_account):
        self.agency_id = checking_account.agency_id
        self.checking_account = checking_account
        self._agency_cash = 10_000
        self._transactions = []
        self.clients = []

    @staticmethod
    def _get_current_date_and_time():
        return datetime.now().strftime('%d/%m/%Y at %H:%M:%S')

    def _check_if_can_withdraw_agency(self, value):
        if self._agency_cash - value < 0:
            return False

        return True

    def _check_if_is_client(self, person_id):
        for client_info in self.clients:
            if person_id in client_info:
                return True

            return False

    def _log_transaction(self, person_id, value):
        value = float(f'{value:.2f}')

        date_and_time = Agency._get_current_date_and_time()

        self._transactions.append((
                                'Person ID:', person_id,
                                '| Total borrowed:', value,
                                '| Date:', date_and_time
        ))

    def get_money(self):
        money_to_withdraw = float(input('\nHow much money do you want to withdraw? '))

        has_enough_money = self._check_if_can_withdraw(money_to_withdraw)

        if has_enough_money:
            self.checking_account._balance += money_to_withdraw
            self._agency_cash -= money_to_withdraw

            print('\nTransaction completed!\n')

            self._log_transaction(self.checking_account.person_id, money_to_withdraw)
            self.checking_account._log_transaction('agency', money_to_withdraw)

        else:
            print(f'\nThis agency has not enough money. Available cash: {self.check_agency_cash()}\n')

    def check_agency_cash(self):
        return f'{self._agency_cash:,.2f}'

    def show_transactions_log(self):
        print('\nTransactions made in this agency:\n')

        for log in self._transactions:
            print(*log)

    def become_client(self):
        person_id = self.checking_account.person_id
        is_client = self._check_if_is_client(person_id)

        if is_client:
            print('\nYou are already a client!\n')

        else:
            self.clients.append(('Name:', self.checking_account.person_name,
                                '| ID:', self.checking_account.person_id,
                                '| Balance:', self.checking_account._balance))

            print('\nYou are now a client!\n')

    def show_clients(self):
        print('\nAll clients:\n')

        for client in self.clients:
            print(*client)

        print()


class StandardAgency(Agency):
    def __init__(self, checking_account):
        super().__init__(checking_account)
        self._agency_cash = 50_000


class PremiumAgency(Agency):
    def __init__(self, checking_account):
        super().__init__(checking_account)
        self._agency_cash = 1_000_000

    def become_client(self):
            if self.checking_account._balance >= 200_000:
                super().become_client()

            else:
                print('\nYou do not have enough money to become a premium client.\n')


class VirtualAgency(Agency):
    def __init__(self, website, checking_account):
        super().__init__(checking_account)
        self.website = website
        self._agency_cash = 100_000
        self._paypal_cash = 0

    def _check_if_can_withdraw_paypal(self, value):
        if self._paypal_cash - value < 0:
            return False

        return True

    def check_paypal_cash(self):
        return f'{self._paypal_cash:,.2f}'

    def deposit_on_paypal(self):
        money_to_paypal = float(input('\nHow much money do you want to send to PayPal? '))

        has_enough_money = self._check_if_can_withdraw_agency(money_to_paypal)

        if has_enough_money:
            self._agency_cash -= money_to_paypal
            self._paypal_cash += money_to_paypal

            print('\nTransaction completed!\n')

        else:
            print(f'\nThis agency has not enough money. Available cash: {self.check_agency_cash()}\n')

    def take_from_paypal(self):
        money_to_take_away = float(input('\nHow much money do you want to take? '))

        has_enough_money = self._check_if_can_withdraw_paypal(money_to_take_away)

        if has_enough_money:
            self._agency_cash += money_to_take_away
            self._paypal_cash -= money_to_take_away

            print('\nTransaction completed!\n')

        else:
            print(f'\nYour PayPal has not enough money. Available cash: {self.check_paypal_cash()}\n')
