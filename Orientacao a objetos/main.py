from checking_account_class import CheckingAccount
from credit_card_class import CreditCard
from agency_classes import Agency, StandardAgency, PremiumAgency, VirtualAgency

my_account = CheckingAccount('Álvaro', '111.222.333-44', '0001', '12345')
destination_account = CheckingAccount('Nicolas', '555.666.777-88', '0002', '67890')

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
        my_account.transfer(destination_account)

    elif user_choice == '5': break

    else: print('\nInvalid option.\n')

my_account.show_transactions_log()
destination_account.show_transactions_log()

my_credit_card = CreditCard(my_account)
secondary_credit_card = CreditCard(my_account)

my_account.show_credit_cards()

my_credit_card.password = '1792'

my_account.show_credit_cards()

agency_1 = Agency(my_account)

while True:
    print('Get cash - 1 | ' \
          'Check your balance - 2 | ' \
          'Check agency cash - 3 | ' \
          'Become a client - 4 | ' \
          'Show all clients - 5 | ' \
          'Finish - 6')

    user_choice = input('Choose an option: ')

    if user_choice == '1':
        agency_1.get_money()

    elif user_choice == '2':
        balance = my_account.check_balance()
        print(f'\nYour current balance is: ${balance}\n')

    elif user_choice == '3':
        agency_cash = agency_1.check_agency_cash()
        print(f'\nTotal cash in agency: ${agency_cash}\n')

    elif user_choice == '4':
        agency_1.become_client()

    elif user_choice == '5':
        agency_1.show_clients()

    elif user_choice == '6': break

    else: print('\nInvalid option.\n')

my_account.show_transactions_log()
agency_1.show_transactions_log()

standard_agency = StandardAgency(my_account)
print(standard_agency.check_agency_cash(), '\n')

premium_agency = PremiumAgency(my_account)
print(premium_agency.check_agency_cash(), '\n')

virtual_agency = VirtualAgency('www.placeholder.com', my_account)
print(virtual_agency.website)
print(virtual_agency.check_agency_cash())

virtual_agency.take_from_paypal()
virtual_agency.deposit_on_paypal()
virtual_agency.take_from_paypal()
virtual_agency.deposit_on_paypal()

# testar com dinheiro insuficiente
my_account.deposit()
premium_agency.become_client()
premium_agency.show_clients()

# testar com dinheiro suficiente
my_account.deposit()
premium_agency.become_client()
premium_agency.show_clients()
