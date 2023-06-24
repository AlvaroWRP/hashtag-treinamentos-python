from datetime import datetime


class Agency:
    def __init__(self, checking_account):
        self.agency_id = checking_account.agency_id
        self.checking_account = checking_account
        self._atm_cash = 10_000  # Automated Teller Machine
        self._transactions = []
        self.clients = []


    @staticmethod
    def _get_current_date_and_time():
        return datetime.now().strftime('%d/%m/%Y at %H:%M:%S')


    def _check_if_can_withdraw(self, value):
        if self._atm_cash - value < 0:
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

        self._transactions.append(('Person ID:', person_id,
                                   '| Total borrowed:', value,
                                   '| Date:', date_and_time))


    def get_money(self):
        money_to_withdraw = float(input('\nHow much money do you want to withdraw? '))

        has_enough_money = self._check_if_can_withdraw(money_to_withdraw)

        if has_enough_money:
            self.checking_account._balance += money_to_withdraw
            self._atm_cash -= money_to_withdraw

            print('\nTransaction completed!\n')

            self._log_transaction(self.checking_account.person_id, money_to_withdraw)
            self.checking_account._log_transaction('atm', money_to_withdraw)

        else:
            print(f'\nThis ATM has not enough money. Cash in ATM: {self.check_atm_cash()}\n')


    def check_atm_cash(self):
        return f'{self._atm_cash:,.2f}'


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
